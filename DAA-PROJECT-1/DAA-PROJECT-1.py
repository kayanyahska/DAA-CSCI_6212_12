import time

def algorithm(n):
    a = [1] * n  # Dummy array, filled with 1s
    b = [1] * n  # Dummy array, filled with 1s
    Sum = 0
    j = 2
    while j < n:
        k = j
        while k < n:
            Sum += a[j] * b[k]
            k = k * k
        j = 2 * j
    return Sum

def measure_time(n):
    start_time = time.time()
    algorithm(n)
    end_time = time.time()
    return end_time - start_time

# Test for different values of n
n_values = [10**i for i in range(2, 9)]  # 10^2 to 10^8

print("n\tTime (seconds)")
print("-----------------------")
for n in n_values:
    execution_time = measure_time(n)
    print(f"{n}\t{execution_time:.6f}")
