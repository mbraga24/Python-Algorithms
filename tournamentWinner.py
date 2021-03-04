# Solution 1:

# Time Complexity: O(n) - n representing the number of competitions
# Space Complexity: O(k) - k representing the number of teams
  # 1) Each team will be at most 30 characters long. That could be represented in equantion as follows:
  #    => O(30k)
  # 2) We initiate the scores hash with 1 extra value before new values are created. This initial value will
  #   assist in keeping the name and the points of the team that has the highest score. But we need to initialize
  #   this key/value pair to an empty string and 0 so we can eventually compare to the first round winner and 
  #   reassign the variable to that current best team. This will be represented in an equation as follows:
  #    => O(k+1) => with 1 being that aditional key we initialize our hash with.
  # 3) Putting it all together our equantion will look like:
  #    => O(30k + 1)
  #   But we drop all constant factors and focus on the long term growth rate of a function, 
  #   since constant facots are not relevant to an asymptotic analysis.
  #     => O(k)

HOME_TEAM_WON = 1

def tournamentWinner(competitions, restuls):
  currentBestTeam = ""
  scores = { currentBestTeam: 0 }

  for idx, competition in enumerate(competitions):
    result = results[idx]
    homeTeam, awayTeam = competition

    winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

    updateScores(winningTeam, 3, scores)

    if scores[winningTeam] > scores[currentBestTeam]:
      currentBestTeam = winningTeam

  return currentBestTeam

def updateScores(team, points, scores):
  if team not in scores:
    scores[team] = 0

  scores[team] += points


competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]

results = [0, 0, 1]

print(tournamentWinner(competitions, results))