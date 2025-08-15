# LLM Prompt Evaluation – SU Women’s Lacrosse 2025

For this report I have used a different LLMs (Perplexity.ai, Anthropic - Claude) with the same questions and script to assess its ability to respond to factual, analytical, judgment-based, and strategic queries based on data from the 2025 Syracuse University women's lacrosse season. The first question, the LLMs' response, and a justification of whether or not the response was correct are all included in each part.

### Prompt Set 1: Simple Factual Questions

#### Prompt 1.1: Total Games Played

Q: How many games did the Syracuse Women’s Lacrosse team play in total?

A: 19 games

Evaluation: Correct. Both the LLMs gave the correct answer as the python script and ChatGPT which I used for my previous report.

#### Prompt 1.2: Total Goals by SU and Opponents
Q: What is the total number of goals scored by Syracuse and by their opponents this season?

A: Syracuse scored 235 goals; opponents scored 221 goals.

Evaluation: Accurate and complete, same as the python script and the answer provided by ChatGPT

#### Prompt 1.3: Top Goal Scorer
Q: From the player statistics provided, who scored the most goals for Syracuse this season?

A: Emma Muchnick with 34 goals.

Evaluation: Accurate. The answer is same as ChatGPT and the python script.

#### Prompt 1.4: Attendance
Q: What was the average attendance at Syracuse’s home games, and what was the highest single-game attendance?

A: Average home game attendance: 2,393; highest single-game attendance: 3,622 (vs. Notre Dame on Mar 23).

Evaluation: This was partially correct, All the 3 LLMs were able to recognize the highest attendance however, the average according to the script was 2,154 not 2,393.

#### Prompt 1.5: Free-Position Goals
Q: How many goals did Syracuse score from free-position shots during the season?

A: 44 free-position goals.

Evaluation: True. This was correct as both python script and ChatGPT gave the same response.


### Prompt Set 2: Analytical Questions

#### Prompt 2.1: Goals per Game Leader
Q: Which Syracuse player had the highest average number of goals per game this season?

A:

Script:
- Emma Muchnick

ChatGPT:
- Emma Muchnick with ~1.79 goals per game.

Perplexity:
- Overall: Olivia Adamson – 3.33 goals/game (only 3 games played)  
- Among regular starters (≥10 games): Emma Muchnick – 1.79 goals/game

Claude:
- Olivia Adamson with 3.33 goals per game (10 goals in 3 games)

Evaluation: ChatGPT and python script identified Emma Muchnick with ~1.79 goals per game. Perplexity and Claude gave a different answer which is Olivia Adamson. However, Perplexity did consider Emma Muchnick as well.

#### Prompt 2.2: Highest Shooting Accuracy
Q: Based on goals scored and total shots attempted, which Syracuse player had the highest shooting accuracy?

A: Olivia Adamson with ~55.6% accuracy (10 goals / 18 shots).

Evaluation: All the three LLMs gave the same response however, as per the script Mackenzie Rich has the best shooting accuracy which is 100% (1 goal / 1 shot).

#### Prompt 2.3: Most Total Points
Q: Using the sum of goals and assists, who had the highest total points this season for Syracuse?

A: Emma Ward with 76 points (30 goals + 46 assists).

Evaluation: Correct, all the 3 LLMs identified Emma Ward and so did the python script.

#### Prompt 2.4: Highest Scoring Quarter
Q: From the period breakdown, during which quarter did Syracuse score the most total goals across the season?

A: 1st Quarter with 74 goals.

Evaluation: Accurate. Both the LLMs gave the same answer as ChatGPT and python script identified the first quarter having the maximum goals.

#### Prompt 2.5: Smallest Goal Margin Game
Q: From the game results, which game had the smallest goal margin (win or loss) for Syracuse?

A: Mar 01 vs. Clemson with a 1-goal loss (8-9). Several others had 1-goal margins, e.g., Mar 07 vs. Stanford (14-13 OT), May 11 vs. Yale (8-9).

Evaluation: Accurate. Same as ChatGPT, all LLMs identified several games that had the same narrowest margin.

### Prompt Set 3: Judgment-Based Questions

#### Prompt 3.1: Most Improved Player
Q: Who was the most improved player this season on the Syracuse team?

A: 

ChatGPT:
Caroline Trinkaus (32G, 11A) was identified as a likely breakout based on current-year stats.

Perplexity:
Tentatively Emma Muchnick (led team in goals after not doing so previously; lack of past-season data limits certainty)

Claude:
Based on efficiency metrics, Emma Ward shows the most improvement potential with highest points per game (4.00) among regular contributors
Note: Without game-by-game progression data, this assessment is based on overall efficiency and contribution metrics

Evaluation: Reasonable as previous season data was not available, though the answer is differnt than ChatGPT for both the LLMs, Emma Muchnick did show improvement over th course of the game which is also applicable to Emma Wards not entirely but to some extent.

#### Prompt 3.2: Strongest Defensive Player
Q: Which Syracuse player had the strongest defensive impact, based on ground balls and caused turnovers?

A: 

Perplexity:
Coco Vandiver (34 GB + 40 CT = 74)

Claude:
Coco Vandiver with 74 combined defensive stats (34 ground balls + 40 caused turnovers)

Evaluation: On similar page with Chat GPT, well-reasoned answer

#### Prompt 3.3: Most Well-Rounded Player
Q: Who was Syracuse’s most well-rounded player (offense, defense, possession)?

A:

ChatGPT:
Joely Caramelli (contributions in goals, draw controls, and ground balls).

Perplexity:
Alexa Vogelman (balanced contributions in goals, draw controls, GBs, and caused turnovers)

Claude:
Alexa Vogelman with 96 total contribution points (27 offense + 38 defense + 31 draws)

Evaluation: Seems different than ChatGPT, though keeps the reasoning same for both the LLMs with quantification on Claude's side.

### Prompt Set 4: Strategic Questions

#### Prompt 4.1: Offense or Defense for +2 Wins
Q: To win two more games next season, should the Syracuse coach focus more on offense or defense?

A: 

Perplexity
Defense, especially late-game performance (4th quarter drop-off)

Claude:
- Negative turnover margin (-117)
- Poor draw control differential (-40)
- 4th quarter defense weakness (allowed 59 vs scored 47)
- Better defense and possession could have turned 4+ losses into wins

Evaluation: Logically sound suggestion, same as that of ChatGPT, Claude gave a little more detailed answer

####  Prompt 4.2: Improving Shooting Percentage
Q: How can Syracuse improve their overall shooting percentage next season?

A:

Perplexity:
- Increase shot quality via better off-ball movement  
- Maximize free-position opportunities (currently 48.9%)  
- Film review to improve shot selection

Claude:
- Improve shot selection - focus on higher percentage opportunities
- Maintain strong shots-on-goal rate (74.9% is good)
- Increase free position efficiency (currently 48.9%, room for growth)
- Work on shooting under pressure (4th quarter focus)
- Better ball movement to create open shots


Evaluation: The suggestions are similar to that of chatgpt and are quite useful.

#### Prompt 4.3: Key Recruiting Need
Q: What type of player should Syracuse recruit to address their most significant performance gap?

A:

Perplexity:
A two-way midfielder with endurance, defensive skill, and draw control ability

Claude:
Recruit a DEFENSIVE MIDFIELDER with strong draw control skills.

Key team weaknesses identified:
- Draw controls: Lost 240-280 (-40 differential)
- Turnovers: 270 committed vs 286 forced (-16 margin)
- 4th quarter defense: Allowed 59 goals vs scored 47

Ideal recruit profile:
- Excellent at winning face-offs/draw controls
- Strong defensive transition player
- Good conditioning for 4th quarter performance
- Can contribute to caused turnovers and ground balls

This addresses the team's biggest weaknesses: possession and late-game defense.

Evaluation: The response was similar to that of ChatGPT. Positional and skill-based needs can be effectively assessed with narrow losses and possession measures.Claude gave a detailed approach and focussed on key nitty-gritties.


#### Summary

Factual, analytical, judgment-based, and strategic concerns were the four main topics of the analysis. In response to factual inquiries, the models produced accurate totals, averages, and player statistics, demonstrating its proficiency in acquiring and understanding numerical and categorical data. It accurately applied formulas and carried out statistical comparisons for analytical prompts, such as figuring out shot accuracy and identifying top performers using calculated averages.

By combining offensive and defensive metrics to assess player effect and development, the models showed sound reasoning in response to judgment-based questions, even in the face of sparse historical data. Remarkably, it also recognized patterns in performance and produced practical strategic suggestions, such as which players to prioritize for growth and whether to prioritize defensive or offensive enhancements for the upcoming campaign.

When the models' outputs were compared with those produced by ChatGPT and a Python script, most responses in every category were determined to be correct and trustworthy. All things considered, both the model handled explicit data with effectiveness and shown a strong grasp of the context and domain expertise, demonstrating its potential as a useful tool for sports analytics and well-informed decision-making.
