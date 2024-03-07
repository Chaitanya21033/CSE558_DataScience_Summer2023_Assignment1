# Part (a): Calculate the true variance of population D

import numpy as np

# Given population D uniformly distributed between 0.01 and 1000
N = 100000  # Total points
D = np.linspace(0.01, 1000, N)  # Population D from 0.01 to 1000

# Calculate the true mean (x_bar) of population D
x_bar = np.mean(D)

# Calculate the true variance (sigma^2) of population D
sigma_squared = np.sum((D - x_bar) ** 2) / N
print("Solution to Part (a)")
print(sigma_squared)

# Part (b): Sampling and computing variances s^2_1, s^2_2, s^2_3

# Sample size
n = 50

# Randomly sample 50 points from D with replacement
sample = np.random.choice(D, size=n, replace=True)

# Calculate the sample mean (mu)
mu = np.mean(sample)

# Compute variances s^2_1, s^2_2, s^2_3
s_squared_1 = np.sum((sample - mu) ** 2) / (n + 1)
s_squared_2 = np.sum((sample - mu) ** 2) / n
s_squared_3 = np.sum((sample - mu) ** 2) / (n - 1)

print("Solution to Part (b)")
print(s_squared_1, s_squared_2, s_squared_3)

# Number of iterations for averaging
iterations = 100

# Initialize sums for averaging variances
sum_s_squared_1 = 0
sum_s_squared_2 = 0
sum_s_squared_3 = 0

# Perform iterations
for _ in range(iterations):
    sample = np.random.choice(D, size=n, replace=True)
    mu = np.mean(sample)
    sum_s_squared_1 += np.sum((sample - mu) ** 2) / (n + 1)
    sum_s_squared_2 += np.sum((sample - mu) ** 2) / n
    sum_s_squared_3 += np.sum((sample - mu) ** 2) / (n - 1)

# Calculate averages
avg_s_squared_1 = sum_s_squared_1 / iterations
avg_s_squared_2 = sum_s_squared_2 / iterations
avg_s_squared_3 = sum_s_squared_3 / iterations


print("Solution to Part (c)")
print(avg_s_squared_1, avg_s_squared_2, avg_s_squared_3)

import matplotlib.pyplot as plt

# Track averages across iterations for plotting
avg_s_squared_1_list = []
avg_s_squared_2_list = []
avg_s_squared_3_list = []
iteration_list = []

# Reset sums for tracking
sum_s_squared_1 = 0
sum_s_squared_2 = 0
sum_s_squared_3 = 0

# Perform iterations again for tracking and plotting
for i in range(1, iterations + 1):
    sample = np.random.choice(D, size=n, replace=True)
    mu = np.mean(sample)
    sum_s_squared_1 += np.sum((sample - mu) ** 2) / (n + 1)
    sum_s_squared_2 += np.sum((sample - mu) ** 2) / n
    sum_s_squared_3 += np.sum((sample - mu) ** 2) / (n - 1)
    
    # Update lists for plotting
    avg_s_squared_1_list.append(sum_s_squared_1 / i)
    avg_s_squared_2_list.append(sum_s_squared_2 / i)
    avg_s_squared_3_list.append(sum_s_squared_3 / i)
    iteration_list.append(i)

# Plotting
plt.figure(figsize=(12, 8))

plt.plot(iteration_list, avg_s_squared_1_list, label='Avg $s^2_1$', marker='o')
plt.plot(iteration_list, avg_s_squared_2_list, label='Avg $s^2_2$', marker='x')
plt.plot(iteration_list, avg_s_squared_3_list, label='Avg $s^2_3$', marker='^')
plt.axhline(y=sigma_squared, color='r', linestyle='-', label='True Variance $\sigma^2$')

plt.xlabel('Iterations')
plt.ylabel('Variance')
plt.title('Comparison of Sample Variance Averages with True Variance')
plt.legend()
plt.grid(True)

plt.show()



