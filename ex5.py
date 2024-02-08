import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

def linearInterpolation(x, b, c):
    return x * b + c

def logarithmicInterpolation(x, a, b):
    return a * np.log(x) + b

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def measure_time(search_function, arr, target, number=100):
    return timeit.timeit(lambda: search_function(arr, target), number=number)

def main():
    sizes = [1000, 2000, 4000, 8000, 16000, 32000]
    iterations = 100

    linear_avg_times = []
    binary_avg_times = []

    for size in sizes:
        total_time_linear = 0
        total_time_binary = 0

        for _ in range(iterations):
            arr = sorted([random.randint(1, 100000) for _ in range(size)])
            target = random.choice(arr)  # Choose a random target in the array

            # Measure time for linear search
            total_time_linear += measure_time(linear_search, arr, target)

            # Measure time for binary search
            total_time_binary += measure_time(binary_search, arr, target)

        # Compute average time for each search
        avg_time_linear = total_time_linear / iterations
        avg_time_binary = total_time_binary / iterations

        linear_avg_times.append(avg_time_linear)
        binary_avg_times.append(avg_time_binary)

    # Plotting
    plt.plot(sizes, linear_avg_times, label='Linear Search')
    plt.plot(sizes, binary_avg_times, label='Binary Search')

    plt.xlabel('Array Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Average Search Time Complexity')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

# 4. Linear search has a linear time complexity, and the interpolating function should be a straight line.
#    Binary search has a logarithmic time complexity, but when measured in terms of the number of iterations, it shows curved behavior. 
#    Because the values are so close to each other and log functions grow very slowly, it appears to be straight. 
#    It is also much faster than linear search. 
