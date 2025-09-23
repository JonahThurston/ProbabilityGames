import random
import matplotlib.pyplot as plt

PRIZES = ['GOAT', 'GOAT', 'CAR']
SAMPLE_SIZES = [10, 30, 50, 70, 90, 100, 250, 500, 750, 1000]

def runGame():
  doors = PRIZES
  random.shuffle(doors)
  n = len(doors)

  initialPick = random.randint(0, n - 1)

  if (doors[initialPick] == 'CAR'):
    return 'staying won!'

  hostPick = (initialPick + 1) % n
  while(doors[hostPick] == 'CAR'):
    hostPick = (hostPick + 1) % n
  
  switchedPick = (initialPick + 1) % n
  while(switchedPick == initialPick or switchedPick == hostPick):
    switchedPick = (switchedPick + 1) % n

  if (doors[switchedPick] == 'CAR'):
    return 'switching won!'
  
  return 'both lost'

switchWinRates = []
stayWinRates = []
lossRates = []

for size in SAMPLE_SIZES:
  switchWins = 0
  stayWins = 0
  losses = 0

  for i in range(size):
    result = runGame()
    if (result == 'switching won!'):
      switchWins += 1
    elif (result == 'staying won!'):
      stayWins += 1
    else:
      losses += 1

    
  switchWinRate = switchWins / size
  switchWinRates.append(switchWinRate)
  stayWinRate = stayWins / size
  stayWinRates.append(stayWinRate)
  lossRate = losses / size
  lossRates.append(lossRate)
  print(f"sample size: {size}    stay: {stayWinRate}    switch: {switchWinRate}   loss: {lossRate}")

import matplotlib.pyplot as plt

# Create evenly spaced positions
x = range(len(SAMPLE_SIZES))

plt.figure(figsize=(10, 6))

plt.plot(x, stayWinRates, marker='o', linestyle='-', label="Stay Win Rate")
plt.plot(x, switchWinRates, marker='o', linestyle='-', label="Switch Win Rate")
plt.plot(x, lossRates, marker='o', linestyle='-', label="Loss Rate")

# Reference lines at theoretical values
plt.axhline(1/3, color='red', linestyle='--', alpha=0.6, label="Theoretical Stay (1/3)")
plt.axhline(2/3, color='green', linestyle='--', alpha=0.6, label="Theoretical Switch (2/3)")

plt.ylim(0, 1)
plt.xticks(x, SAMPLE_SIZES)  # map positions back to labels
plt.xlabel("Sample Size")
plt.ylabel("Rate")
plt.title("Monty Hall Simulation Results (Evenly Spaced Sample Sizes)")
plt.legend()

plt.show()


plt.show()