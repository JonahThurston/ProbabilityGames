import random
import matplotlib.pyplot as plt

# Generate 20 random numbers between 1 and 100
data = [random.randint(1, 100) for _ in range(20)]

# Plot as a histogram
plt.hist(data, bins=10, color="skyblue", edgecolor="black")

plt.title("Histogram of Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()