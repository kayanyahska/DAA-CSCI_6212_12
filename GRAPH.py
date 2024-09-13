import matplotlib.pyplot as plt
import numpy as np

# Data from the Java program output
n_values = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
experimental_times = [0.000000041, 0.000000068, 0.000000105, 0.000000156, 0.000000224, 0.000000315, 0.000000433]

# Calculate theoretical values
def theoretical_complexity(n):
    return np.log2(n) * np.log2(np.log2(n))

theoretical_values = [theoretical_complexity(n) for n in n_values]

# Calculate scaling factor
scaling_factor = experimental_times[0] / theoretical_values[0]

# Calculate scaled theoretical times
scaled_theoretical_times = [tv * scaling_factor for tv in theoretical_values]

# Create the plot
plt.figure(figsize=(12, 8))
plt.loglog(n_values, experimental_times, 'bo-', label='Experimental')
plt.loglog(n_values, scaled_theoretical_times, 'ro-', label='Theoretical')

plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Algorithm Performance: Experimental vs Theoretical')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.2)

# Add annotations for each point
for i, (n, exp_time, theo_time) in enumerate(zip(n_values, experimental_times, scaled_theoretical_times)):
    plt.annotate(f'n={n}\nExp: {exp_time:.2e}\nTheo: {theo_time:.2e}', 
                 (n, exp_time), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center', 
                 va='bottom',
                 bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                 arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

plt.tight_layout()
plt.show()