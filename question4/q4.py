import numpy as np
import matplotlib.pyplot as plt

# Optional: Set a random seed for reproducibility
np.random.seed(42)

def roll_die(k):
    """Simulate a roll of a biased k-faced die."""
    probabilities = np.array([1/(2**(k-1)) if i == 1 or i == k else 1/(2**(i-1)) for i in range(1, k+1)])
    return np.random.choice(range(1, k+1), p=probabilities)

def simulate_rolls(k, num_rolls, num_simulations):
    """Simulate rolling the die multiple times and calculate sums of face values."""
    sums = [sum(roll_die(k) for _ in range(num_rolls)) for _ in range(num_simulations)]
    return sums

def plot_histogram(sums, title, filename):
    """Plot a frequency distribution histogram of the sums and save to a file."""
    plt.hist(sums, bins=range(min(sums), max(sums) + 1, 1), alpha=0.75, edgecolor='black')
    plt.title(title)
    plt.xlabel('Sum of face values')
    plt.ylabel('Frequency')
    plt.savefig(filename)  # Save the plot as a file
    plt.close()  # Close the plot to free memory

def bowleys_coefficient(sums):
    """Compute Bowley's coefficient for the given sums."""
    q1 = np.percentile(sums, 25)
    q3 = np.percentile(sums, 75)
    median = np.median(sums)
    return (q1 - 2*median + q3) / (q3 - q1)

# Part (a): k=4, rolling 4 times, 1000 simulations
k = 4
num_rolls_a = 4
num_simulations = 1000
sums_a = simulate_rolls(k, num_rolls_a, num_simulations)
plot_histogram(sums_a, "Frequency Distribution for k=4, 4 rolls", "histogram_k4_4rolls.png")
print(bowleys_coefficient(sums_a))


# Part (b): k=4, rolling 8 times, 1000 simulations
num_rolls_b = 8
sums_b = simulate_rolls(k, num_rolls_b, num_simulations)
plot_histogram(sums_b, "Frequency Distribution for k=8, 8 rolls", "histogram_k8_8rolls.png")
print(bowleys_coefficient(sums_b))

k_c = 16
num_rolls_c = 4
sums_c = simulate_rolls(k_c, num_rolls_c, num_simulations)
plot_histogram(sums_c, "Frequency Distribution for k=16, 16 rolls", "histogram_k16_16rolls.png")
print(bowleys_coefficient(sums_c))