import random
import matplotlib.pyplot as plt
import numpy as np

def runBattle(attackerDice, defenderDice):
  attackerRolls = []
  for _ in range(attackerDice):
    attackerRolls.append(random.randint(1,6))
  attackerRolls.sort(reverse=True)

  defenderRolls = []
  for _ in range(defenderDice):
    defenderRolls.append(random.randint(1,6))
  defenderRolls.sort(reverse=True)

  attackerLosses = 0
  defenderLosses = 0
  i = 0
  while(i < len(attackerRolls) and i < len(defenderRolls)):
    if (attackerRolls[i] > defenderRolls[i]):
      defenderLosses += 1
    else:
      attackerLosses += 1
    i += 1
  
  return (attackerLosses, defenderLosses)

def runBattlesTillEnd(attackerSize, defenderSize):
  while attackerSize >= 2 and defenderSize >= 1:
    attackerDice = min(attackerSize - 1, 3)
    defenderDice = min(defenderSize, 2)

    (attackerLosses, defenderLosses) = runBattle(attackerDice, defenderDice)

    attackerSize -= attackerLosses
    defenderSize -= defenderLosses
  
  return (attackerSize, defenderSize)

def diceNumMatchup(sampleSize = 10000):
  print("dice number matchups")
  attackerOptions = [1,2,3]
  defenderOptions = [1,2]

  for attackerDice in attackerOptions:
    for defenderDice in defenderOptions:
      totalAttackerLosses = 0
      totalDefenderLosses = 0
      for _ in range(sampleSize):
        (attackerLosses, defenderLosses) = runBattle(attackerDice, defenderDice)
        totalAttackerLosses += attackerLosses
        totalDefenderLosses += defenderLosses
      attackerLossAvg = totalAttackerLosses / sampleSize
      defenderLossAvg = totalDefenderLosses / sampleSize
      print(f"  {attackerDice}/{defenderDice} ALoss: {attackerLossAvg} DLoss: {defenderLossAvg}")

def attackerWinChance(sampleSize = 10000):
  attackerOptions = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
  defenderSize = 5

  winRates = []
  for attackerSize in attackerOptions:
    wins = 0
    for _ in range(sampleSize):
      (newAttackerSize, newDefenderSize) = runBattlesTillEnd(attackerSize, defenderSize)
      if(newAttackerSize >= 2):
        wins += 1
    winRate = wins / sampleSize
    winRates.append(winRate)

  # Plot results
  plt.figure(figsize=(8,5))
  plt.plot(attackerOptions, winRates, marker='o', linestyle='-', label="Win Rate")
  plt.title(f"Attacker Win Chance vs. Number of Attackers (Defenders = {defenderSize})")
  plt.xlabel("Number of Attackers")
  plt.ylabel("Win Rate")
  plt.ylim(0, 1)  # win rate between 0 and 1
  plt.xticks(attackerOptions)  # x-axis ticks for each attacker size
  plt.yticks(np.arange(0, 1.1, 0.1))  # y-axis ticks every 10%
  plt.grid(True, linestyle='--', alpha=0.6)
  plt.show()

def equalArmySizeAnalysis(sampleSize = 10000):
  armySize = 10

  countResultInstances = {}
  for _ in range(sampleSize):
    (newAttackerSize, newDefenderSize) = runBattlesTillEnd(armySize, armySize)
    result = str(newAttackerSize) + 'to' + str(newDefenderSize)
    if result in countResultInstances:
      countResultInstances[result] += 1
    else:
      countResultInstances[result] = 0

  resultAverages = {key: value / sampleSize for key, value in countResultInstances.items()}

diceNumMatchup()
attackerWinChance()
equalArmySizeAnalysis()
