#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the datasets (assuming you've saved them as .csv files)
team_stats = pd.read_csv("./teamstats.csv")
player_stats = pd.read_csv("./playerstats.csv")
score_breakdown = pd.read_csv("./scorebreakdown.csv")
goal_breakdown = pd.read_csv("./goalbreakdown.csv")


# In[3]:


# Q1: Number of games played
games_played = len(score_breakdown)
print("Games played:", games_played)

# Q2: Total goals scored by Syracuse and opponents
total_goals_su = team_stats.loc[team_stats['TEAM STATISTICS'] == 'Total Goals', 'SU'].values[0]
total_goals_opp = team_stats.loc[team_stats['TEAM STATISTICS'] == 'Total Goals', 'OPP'].values[0]
print("Total goals - Syracuse:", total_goals_su)
print("Total goals - Opponents:", total_goals_opp)

# Q3: Top scorer
# Convert all relevant stat columns to numeric safely
cols_to_numeric = ['GP', 'G', 'A', 'Pts', 'Sh']
player_stats[cols_to_numeric] = player_stats[cols_to_numeric].apply(pd.to_numeric, errors='coerce')

player_stats.columns = player_stats.columns.str.strip()

# Convert 'G' column to numeric (handle "U" or missing as NaN)
player_stats['G'] = pd.to_numeric(player_stats['G'], errors='coerce')

# Find top scorer

top_scorer = player_stats.loc[player_stats['G'] == player_stats['G'].max()]
print("Top scorer:\n", top_scorer[['PLAYER', 'G']])
# Q4: Average attendance for home games
# Filter home games by excluding "at" and "vs" games# Convert attendance column to numeric

# Convert attendance column to numeric
score_breakdown['Att.'] = pd.to_numeric(score_breakdown['Att.'], errors='coerce')

# Filter home games: exclude games with "at" or "vs" in Opponent column (i.e., away or neutral games)
home_games = score_breakdown[~score_breakdown['Opponent'].str.contains(r'\bat\b|\bvs\b', case=False, na=False)]

# Sum attendance and calculate average
home_attendance_total = home_games['Att.'].dropna().sum()
average_home_attendance = home_attendance_total / len(home_games)

print("Average home attendance:", round(average_home_attendance))


fp_goals = int(team_stats.loc[team_stats['TEAM STATISTICS'] == 'Free-position', 'SU'].values[0])
print("Free-position goals scored by Syracuse:", fp_goals)


# In[4]:


# Remove any rows where GP is zero or NaN to avoid divide-by-zero
player_stats = player_stats[player_stats['GP'] > 0]

# Q6: Player with highest goals per game
player_stats['GPG'] = player_stats['G'] / player_stats['GP']
top_gpg = player_stats.loc[player_stats['GPG'].idxmax()]
print("Highest Goals/Game:", top_gpg['PLAYER'], "with", round(top_gpg['GPG'], 2))

# Q7: Player with highest shooting accuracy (avoid division by zero or NaNs)
player_stats = player_stats[player_stats['Sh'] > 0]
player_stats['ShotAccuracy'] = player_stats['G'] / player_stats['Sh']
top_accuracy = player_stats.loc[player_stats['ShotAccuracy'].idxmax()]
print("Best shooting accuracy:", top_accuracy['PLAYER'], "with", round(top_accuracy['ShotAccuracy'], 2))

# Q8: Most total points (G + A)
player_stats['TotalPoints'] = player_stats['G'] + player_stats['A']
most_points = player_stats.loc[player_stats['TotalPoints'].idxmax()]
print("Most total points:", most_points['PLAYER'], "with", int(most_points['TotalPoints']))

# Q9: Quarter with most goals (assuming column is a Series of 6 values)
goal_quarters = ['1st', '2nd', '3rd', '4th', 'OT1', 'OT2']
goal_values = goal_breakdown['Goals by Syracuse'].head(6).fillna(0).astype(int).tolist()
goal_cols = dict(zip(goal_quarters, goal_values))

most_goals_q = max(goal_cols, key=goal_cols.get)
print("Quarter with most Syracuse goals:", most_goals_q, "with", goal_cols[most_goals_q], "goals")


# In[ ]:




