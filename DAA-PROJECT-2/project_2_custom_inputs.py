import time


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        print(array)

def finding_the_median_of_medians(array, group_size):
    array_length = array.__len__()
    if array_length<=group_size:
        insertion_sort(array)
        return array[array_length//2]
    median_array = []
    for i in range(0,array_length, group_size):
        group_array = array[i:i+group_size]
        insertion_sort(group_array)
        median_array.append(group_array[(group_array.__len__())//2])
    return finding_the_median_of_medians(median_array, group_size)

def partition(array, pivot):
    less = [x for x in array if x<pivot]
    equal = [x for x in array if x==pivot]
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

def file_reader(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip().split(': ')[1])
        array = list(map(int, file.readline().strip().split(': ')[1].split()))
        k = int(file.readline().strip().split(': ')[1])
        group_size = int(file.readline().strip().split(': ')[1])
    return n, array, k, group_size


if __name__ == '__main__':
    #n = int(input("Enter the number of elements in an array"))
    #array = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    #k = int(input("Enter the value of k (0-based index for k-th smallest): "))
    #group_size = int(input("Enter the size of the groups for median finding: "))
    filename = input("Enter the name of the input file: ")
    n, array, k, group_size = file_reader(filename)

    if k < 0 or k >= n:
        print("Invalid value of k. It should be between 0 and", n - 1)
    elif group_size <= 0:
        print("Group size must be a positive integer.")
    else:
        start_time = time.perf_counter_ns()
        result = quickselect(array, k, group_size)
        end_time = time.perf_counter_ns()
        print(f"The {k + 1}-th smallest element is: {result}")
