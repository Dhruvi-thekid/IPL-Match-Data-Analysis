# 🏏 IPL Match Data Analysis

A data analytics project that explores Indian Premier League (IPL) match data using Python, Pandas, and Streamlit.

The project analyzes match performance, team statistics, scoring trends, bowling performance, toss decisions, and venue statistics through exploratory data analysis and an interactive dashboard.

---

## 📌 Project Overview

This project uses IPL ball-by-ball match data to identify useful patterns and trends across different IPL seasons.

The analysis includes:

- Team performance and win percentage
- Season-wise scoring trends
- Top wicket-takers
- Toss decision impact
- Venue-wise match and scoring analysis
- Interactive filtering by season, team, and venue

---

## 📊 Dataset

The original dataset contains:

- **295,732** ball-by-ball records
- **64** columns
- **1,243** matches
- IPL seasons from **2007/08 to 2026**

The dataset contains information about:

- Matches
- Teams
- Players
- Runs
- Wickets
- Venues
- Toss decisions
- Match results
- Seasons

The original and cleaned CSV files are not included in the GitHub repository because of their large file size.

---

## 🧹 Data Cleaning

The data preparation process included:

- Removing unnecessary columns
- Handling missing values
- Standardizing team names
- Converting date and season fields
- Checking unique values and data types
- Creating a cleaned dataset for analysis
- Creating a dashboard-specific dataset

---

## 🔎 Exploratory Data Analysis

The project investigates several aspects of IPL performance.

### Team Performance

Team matches played, wins, and win percentage were calculated to compare historical team performance.

### Season Scoring

Total runs and average runs per match were calculated for each IPL season.

### Bowling Performance

The top wicket-taking bowlers were identified using wicket-level data.

### Toss Analysis

The relationship between toss decisions and match outcomes was analyzed.

### Venue Analysis

Venues were compared based on matches played, total runs, and average runs per match.

---

## 📈 Interactive Dashboard

The project includes a Streamlit dashboard with:

- KPI cards
- Season filter
- Team filter
- Venue filter
- Team performance analysis
- Win percentage chart
- Season scoring trend
- Top 10 wicket-takers
- Toss analysis
- Filtered dataset information

### Dashboard Preview




---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Jupyter Notebook
- VS Code

---

## 📂 Project Structure

```text
IPL-Match-Data-Analysis/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── IPL.csv
│   └── IPL_Dashboard_Data.csv
│
├── notebooks/
│   └── ipl_analysis.ipynb
│
├── .gitignore
├── requirements.txt
└── README.md
