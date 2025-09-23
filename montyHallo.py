import random
import matplotlib.pyplot as plt

PRIZES = ['GOAT', 'GOAT', 'CAR']
SAMPLE_SIZES = [1, 10, 100, 1000, 10000, 100000, 1000000]

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

plt.figure(figsize=(10, 6))
plt.plot(SAMPLE_SIZES, stayWinRates, marker='o', label="Stay Win Rate")
plt.plot(SAMPLE_SIZES, switchWinRates, marker='o', label="Switch Win Rate")
plt.plot(SAMPLE_SIZES, lossRates, marker='o', label="Loss Rate")

plt.xscale('log')  # log scale makes the growth in sample size clearer
plt.ylim(0, 1)     # probabilities range between 0 and 1
plt.xlabel("Sample Size (log scale)")
plt.ylabel("Rate")
plt.title("Monty Hall Simulation Results")
plt.legend()

plt.show()