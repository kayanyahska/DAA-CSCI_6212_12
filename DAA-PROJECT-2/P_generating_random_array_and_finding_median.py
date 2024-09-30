import time
import random

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def finding_the_median_of_medians(array, group_size):
    array_length = len(array)
    if array_length <= group_size:
        insertion_sort(array)
        return array[array_length // 2]
    median_array = []
    for i in range(0, array_length, group_size):
        group_array = array[i:i + group_size]
        insertion_sort(group_array)
        median_array.append(group_array[len(group_array) // 2])
    return finding_the_median_of_medians(median_array, group_size)

def partition(array, pivot):
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]
    return less, equal, greater

def quickselect(array, k, group_size):
    if len(array) == 1:
        return array[0]

    pivot = finding_the_median_of_medians(array, group_size)
    less, equal, greater = partition(array, pivot)

    if k < len(less):
        return quickselect(less, k, group_size)
    elif k < len(less) + len(equal):
        return equal[0]
    else:
        return quickselect(greater, k - len(less) - len(equal), group_size)

def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

if __name__ == '__main__':
    sizes = [20, 50, 100, 200, 300, 400, 500]
    group_size = 5
    results = []

    # Open the file once before the loop
    with open("results.txt", "w") as file:
        for n in sizes:
            array = generate_random_array(n)
            k = n // 2  # k is the index for the median value

            start_time = time.perf_counter_ns()
            result = quickselect(array, k, group_size)
            end_time = time.perf_counter_ns()

            time_taken = (end_time - start_time) / 1_000_000  # Convert to milliseconds
            result_line = f"n = {n}, Median = {result}, Time taken = {time_taken:.2f} ms"
            results.append(result_line)

            # Print only the result to console
            print(result_line)

            # Write the result and array to the file
            file.write(result_line + "\n")
            file.write(f"Array: {array}\n")  # Write the array values to the file

    print("Results written to results.txt")