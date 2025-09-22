import random
import matplotlib.pyplot as plt

SAMPLE_SIZES = [100, 1000, 10000, 100000, 1000000]

def runGame():
  numFlips = 0

  while True:
    numFlips += 1
    result = random.choice(["HEADS", "TAILS"])
    if result == "TAILS":
      break

  winnings = 2 ** numFlips
  return winnings

averages = []

for size in SAMPLE_SIZES:
  total = 0
  for i in range(size):
    total += runGame()
  average = total / size
  averages.append(average)
  print(f"sample size: {size}    sum: {total}    avg: {average}")

# ngl, I made chat do the plots, because idk matplotlib
plt.figure(figsize=(8, 5))
plt.plot(SAMPLE_SIZES, averages, marker="o")
plt.xscale("log")  # log scale makes sense here
plt.xlabel("Sample Size (log scale)")
plt.ylabel("Average Winnings")
plt.title("St. Petersburg Paradox Simulation")
plt.grid(True)
plt.show()