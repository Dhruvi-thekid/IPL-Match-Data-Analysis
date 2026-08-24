import streamlit as st
import pandas as pd


# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="IPL Data Analytics",
    page_icon="🏏",
    layout="wide"
)


# ============================================
# LOAD DATA
# ============================================

df = pd.read_csv("data/IPL_Dashboard_Data.csv")

# Make season consistent
df["season"] = df["season"].astype(str)


# ============================================
# TITLE
# ============================================

st.title("🏏 IPL Match Data Analytics Dashboard")

st.write(
    "Interactive analysis of IPL matches, teams, players, "
    "venues and scoring trends."
)


# ============================================
# FILTERS
# ============================================

st.divider()

st.subheader("🔎 Dashboard Filters")

col1, col2, col3 = st.columns(3)


# ---------- Season ----------

with col1:

    seasons = df["season"].dropna().unique().tolist()

    selected_season = st.selectbox(
        "Select Season",
        ["All Seasons"] + seasons
    )


# ---------- Team ----------

with col2:

    teams = sorted(
        df["batting_team"].dropna().unique()
    )

    selected_team = st.selectbox(
        "Select Team",
        ["All Teams"] + teams
    )


# ---------- Venue ----------

with col3:

    venues = sorted(
        df["venue"].dropna().unique()
    )

    selected_venue = st.selectbox(
        "Select Venue",
        ["All Venues"] + venues
    )


# ============================================
# APPLY FILTERS
# ============================================

filtered_df = df.copy()


# Season filter
if selected_season != "All Seasons":

    filtered_df = filtered_df[
        filtered_df["season"] == selected_season
    ]


# Team filter
if selected_team != "All Teams":

    filtered_df = filtered_df[
        (filtered_df["batting_team"] == selected_team) |
        (filtered_df["bowling_team"] == selected_team)
    ]


# Venue filter
if selected_venue != "All Venues":

    filtered_df = filtered_df[
        filtered_df["venue"] == selected_venue
    ]


# ============================================
# FILTERED KPI CALCULATIONS
# ============================================

filtered_matches = filtered_df["match_id"].nunique()

filtered_runs = filtered_df["runs_total"].sum()

filtered_wickets = (
    filtered_df["wicket_kind"].notna().sum()
)

filtered_deliveries = len(filtered_df)


# ============================================
# KPI CARDS
# ============================================

st.divider()

st.subheader("📊 Selected Data Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🏏 Matches",
    filtered_matches
)

col2.metric(
    "🔥 Runs",
    filtered_runs
)

col3.metric(
    "🎯 Wickets",
    filtered_wickets
)

col4.metric(
    "📦 Deliveries",
    filtered_deliveries
)

# ============================================
# TEAM PERFORMANCE
# ============================================

st.divider()

st.subheader("🏆 Team Performance")

match_data = (
    filtered_df[
        [
            "match_id",
            "batting_team",
            "bowling_team",
            "match_won_by"
        ]
    ]
    .drop_duplicates("match_id")
)

# Count matches played
batting_matches = (
    match_data
    .groupby("batting_team")["match_id"]
    .nunique()
)

bowling_matches = (
    match_data
    .groupby("bowling_team")["match_id"]
    .nunique()
)

matches_played = (
    batting_matches
    .add(bowling_matches, fill_value=0)
)

# Count wins
wins = (
    match_data["match_won_by"]
    .value_counts()
)

team_stats = pd.DataFrame({
    "matches_played": matches_played,
    "wins": wins
}).fillna(0)

team_stats["win_percentage"] = (
    team_stats["wins"] /
    team_stats["matches_played"]
) * 100

team_stats = (
    team_stats
    .reset_index()
    .rename(columns={"index": "team"})
    .sort_values(
        "win_percentage",
        ascending=False
    )
)

st.dataframe(
    team_stats,
    use_container_width=True
)

# ============================================
# TEAM WIN PERCENTAGE CHART
# ============================================

chart_data = (
    team_stats
    .set_index("team")["win_percentage"]
    .sort_values(ascending=True)
)

st.bar_chart(chart_data)

# ============================================
# SEASON SCORING TREND
# ============================================

st.divider()

st.subheader("📈 Season-wise Scoring Trend")

season_stats = (
    filtered_df
    .groupby("season")
    .agg(
        matches=("match_id", "nunique"),
        total_runs=("runs_total", "sum")
    )
    .reset_index()
)

season_stats["runs_per_match"] = (
    season_stats["total_runs"] /
    season_stats["matches"]
)

season_stats = season_stats.sort_values("season")

st.dataframe(
    season_stats,
    use_container_width=True
)

st.line_chart(
    season_stats.set_index("season")["runs_per_match"]
)

# ============================================
# TOP 10 WICKET-TAKERS
# ============================================

st.divider()

st.subheader("🎯 Top 10 Wicket-Takers")

bowler_stats = (
    filtered_df[
        filtered_df["wicket_kind"].notna()
    ]
    .groupby("bowler")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(bowler_stats)

# ============================================
# TOSS DECISION IMPACT
# ============================================

st.divider()

st.subheader("🪙 Toss Decision Impact")

toss_data = (
    filtered_df[
        filtered_df["toss_decision"].notna()
    ]
    .groupby("toss_decision")
    .agg(
        matches=("match_id", "nunique"),
        wins=("match_won_by", "count")
    )
    .reset_index()
)

st.bar_chart(
    toss_data.set_index("toss_decision")["matches"]
)


# ============================================
# FILTER RESULT
# ============================================

st.write(
    "Showing",
    len(filtered_df),
    "ball-by-ball records."
)

st.write(
    "Selected Season:",
    selected_season
)

st.write(
    "Selected Team:",
    selected_team
)

st.write(
    "Selected Venue:",
    selected_venue
)


# ============================================
# DATASET PREVIEW
# ============================================

st.divider()

st.subheader("Dataset Preview")

st.dataframe(
    filtered_df.head(10),
    use_container_width=True
)