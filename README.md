Adapting League of Legends Elo Rating for UFC Fighters
======================================================

***Who's the real GOAT of the UFC? Is it GSP like everyone says? Is it somehow Mighty Mouse? Is Jon Jones as good as Dana White says he is?***
**What better way to answer this question than with an objective Elo engine? Better yet, let's use the League of Legends ranking system to rank fighters!**

# Elo Calculation
---
Unfortunately, Riot keeps League's current ranking system a secret, so I'll be using their Season 2 ranking system which follows the Elo system, and then applying the current rank percentiles to the calculated ranks.

Elo from a fight is calculated with the following procedure:
For fighters $A$ and $B$ with Elo ratings of $R_a$ and $R_b$, the expected chance $E_a$ for $A$ winning is given by the formula $E_a = 1/(1 + 10^((R_b - R_a)/400))$.

The change in elo for $A$ is thus given by $R_(a, new) = R_(a, old) + K(S_a - E_a)$, where $K$ is constant representing cap on elo gain or loss, and $S_a$ is the result of the game; 1 for win, 0 for loss, and 0.5 for draw/no contest.
The wiki says that all players start with an elo of 1200, and their $K$ starts around 100 and decreases quickly to around 25. Our engine copies this, and calculates $K$ using a formula that takes in the number of previous fights:
$floor + (start - floor) * e^(-decayRate * number_of_games)$
where $floor = 25, start = 100, and decayRate$ is arbitrarily set to $0.1$. Though this function is arbitrary, it mirrors how $K$ behaves in League's ranking system.

After Elos are calculated for all fighters, we simply take the percentiles for each League rank (found here for Season 14: https://www.leagueofgraphs.com/rankings/rank-distribution) and apply them to the percentile of fighters. For example, if the top 1% of League players are Challenger, then the top 1% of fighters are assigned Challenger rank, and so on.

# Data Scraping
---
Data is scraped from the wikipedia page for past UFC fights: https://en.wikipedia.org/wiki/List_of_UFC_events. Results are in All_fight_reslts.csv.
All fights up to **UFC 310** are included.

# Results
---
3 tables are made: Current_Elos, which has all the fighters' current Elos, Peak_Elos, which has all the fighters' peak elos, and Historical_Elos, which has the calculated elos for all fighters after every fight in their career.
The fighters with the highest Elos right now are Jon Jones (1645), Georges St-Pierre (1570), and Islam Makhachev (1587).
The fighters with the highest Elos at their peak are Jon Jones (1645), Kamaru Usman (1612), and Chris Wieldman (1598).

Turns out Dana's glazing of **Jon Jones** is actually warranted.
🐐 GOAT! 🐐
![Jon Jones](jon_jones.webp)
