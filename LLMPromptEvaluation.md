# LLM Prompt Evaluation – SU Women’s Lacrosse 2025


This document provides an overview of a set of carefully constructed prompts intended to assess ChatGPT's ability to respond to factual, analytical, judgment-based, and strategic queries based on data from the 2025 Syracuse University women's lacrosse season. The first question, the LLM's response, and a justification of whether or not the response was correct are all included in each part.


### Prompt Set 1: Simple Factual Questions

The purpose of these questions was to assess the LLM's memory and summarization of fundamental statistics from the dataset without the need for deduction or reasoning. 

I did a python script to verify the answers provided by LLM to understand its accuracy.

#### Prompt 1.1: Total Games Played

Q: How many games did the Syracuse Women’s Lacrosse team play in total?

A: 19 games

Evaluation: Correct. The right amount of games was successfully obtained and reported by the LLM. The python script retrived the same count.

#### Prompt 1.2: Total Goals by SU and Opponents
Q: What is the total number of goals scored by Syracuse and by their opponents this season?

A: Syracuse scored 235 goals; opponents scored 221 goals.

Evaluation: Accurate and complete Both team totals were appropriately and alignedly extracted by the LLM.


#### Prompt 1.3: Top Goal Scorer
Q: From the player statistics provided, who scored the most goals for Syracuse this season?

A: Emma Muchnick with 34 goals.

Evaluation: Correct. The right individual stat leader was identified and selected by the LLM.

#### Prompt 1.4: Attendance
Q: What was the average attendance at Syracuse’s home games, and what was the highest single-game attendance?

A: Average home game attendance: 2,393; highest single-game attendance: 3,622 (vs. Notre Dame on Mar 23).

Evaluation: This was partially correct, the LLM was able to recognize the highest attendance however, the average according to the scrip was 2,154 not 2,393.

#### Prompt 1.5: Free-Position Goals
Q: How many goals did Syracuse score from free-position shots during the season?

A: 44 free-position goals.

Evaluation: True. The dataset is directly matched, therefore no inference is necessary.


### Prompt Set 2: Analytical Questions

These questions evaluate the LLM's proficiency in basic computation and the interpretation of team or player statistics.

#### Prompt 2.1: Goals per Game Leader
Q: Which Syracuse player had the highest average number of goals per game this season?

A: Emma Muchnick with ~1.79 goals per game.

Evaluation: Correct. The LLM correctly applied the goals-per-game formula.

#### Prompt 2.2: Highest Shooting Accuracy
Q: Based on goals scored and total shots attempted, which Syracuse player had the highest shooting accuracy?

A: Olivia Adamson with ~55.6% accuracy (10 goals / 18 shots).

Evaluation: Not completely accurate. As per the script Mackenzie Rich has the best shooting accuracy which is 100% (1 goal / 1 shot).

#### Prompt 2.3: Most Total Points
Q: Using the sum of goals and assists, who had the highest total points this season for Syracuse?

A: Emma Ward with 76 points (30 goals + 46 assists).

Evaluation: Accurate. The LLM properly summed the stats and identified the correct player with the highest points.

#### Prompt 2.4: Highest Scoring Quarter
Q: From the period breakdown, during which quarter did Syracuse score the most total goals across the season?

A: 1st Quarter with 74 goals.

Evaluation: Accurate. Using a straightforward comparison, the LLM selected the appropriate quarter.

#### Prompt 2.5: Smallest Goal Margin Game
Q: From the game results, which game had the smallest goal margin (win or loss) for Syracuse?

A: Mar 01 vs. Clemson with a 1-goal loss (8-9). Several others had 1-goal margins, e.g., Mar 07 vs. Stanford (14-13 OT), May 11 vs. Yale (8-9).

Evaluation: Accurate. The LLM explicitly identified several games that had the same narrowest margin.

### Prompt Set 3: Judgment-Based Questions

These questions call for evaluative reasoning, and answers are evaluated according to their use of reasoning and statistics.

#### Prompt 3.1: Most Improved Player
Q: Who was the most improved player this season on the Syracuse team?

A: Caroline Trinkaus (32G, 11A) was identified as a likely breakout based on current-year stats.

Evaluation: Reasonable. Although previous season data was not available, LLM provided a reasonable estimate based on available parameters.

#### Prompt 3.2: Strongest Defensive Player
Q: Which Syracuse player had the strongest defensive impact, based on ground balls and caused turnovers?

A: Coco Vandiver (34 GB + 40 CT = 74)

Evaluation: Well-reasoned, with honorable mentions provided for depth.

#### Prompt 3.3: Most Well-Rounded Player
Q: Who was Syracuse’s most well-rounded player (offense, defense, possession)?

A: Joely Caramelli (contributions in goals, draw controls, and ground balls).

Evaluation: Sound judgment based on stat balance across categories. Coco Vandiver was acknowledged for strong defense.

### Prompt Set 4: Strategic Questions

These prompt assess performance at the team level and offer suggestions or insights for future planning.

#### Prompt 4.1: Offense or Defense for +2 Wins
Q: To win two more games next season, should the Syracuse coach focus more on offense or defense?

A: Defense, specifically in the 4th quarter where they allowed the most goals.

Evaluation:Sound logic supported by goal differential, turnover margin, and 4th-quarter trends.

####  Prompt 4.2: Improving Shooting Percentage
Q: How can Syracuse improve their overall shooting percentage next season?

A: Suggestions included better off-ball movement, smarter shot selection, and draw control improvements.

Evaluation: Thoughtful and useful. The suggestions aligned with the performance disparities.

#### Prompt 4.3: Key Recruiting Need
Q: What type of player should Syracuse recruit to address their most significant performance gap?

A: A defensive midfielder with high ground ball recovery, turnover creation, and clutch shooting ability.

Evaluation: Narrow losses and possession metrics provides an excellent assessment of positional and skill-based needs.


#### Summary

Factual, analytical, judgment-based, and strategic prompts were the four areas in which the Large Language Model (LLM) continuously produced excellent results. The algorithm correctly retrieved numerical and categorical data, including totals, averages, and player-specific measures, while answering factual questions. It accurately applied formulas and carried out statistical comparisons for analytical queries, such as calculating goal-to-shot ratios or recognizing top performers using computed averages.

Even with inadequate facts, the LLM showed strong thinking in the judgment-based area. It made logical qualitative judgments, such as weighing defense, goal, and assist statistics in tandem to estimate player impact. Most remarkably, the model demonstrated the capacity to decipher data trends and patterns and suggest workable solutions in response to strategic cues. This included recommendations on which players to continue develop based on performance gaps or whether the club should concentrate on offensive or defensive improvements.

All things considered, the LLM demonstrated contextual awareness and domain-relevant insight in addition to handling explicit data effectively, making it a promising tool for enhancing sports analytics and decision-making.


### Visualization by ChatGPT

1. Top Goal Scorers

![Chart](https://github.com/user-attachments/assets/2ed9fa45-24ba-47cc-b800-4432d2966b28)




2. Syracuse Vs Opponents (Goals, Shots, Assists)

<img width="3000" height="1800" alt="chart1_stacked_bar" src="https://github.com/user-attachments/assets/53ae3968-ca62-4100-8372-8c3b68b052ef" />
