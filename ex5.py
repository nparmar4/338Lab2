import timeit
import random

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

    for size in sizes:
        arr = sorted([random.randint(1, 100000) for _ in range(size)])
        total_time_linear = 0
        total_time_binary = 0

        for _ in range(iterations):
            target = random.choice(arr)

            # Measure time for linear search
            total_time_linear += measure_time(linear_search, arr, target)

            # Measure time for binary search
            total_time_binary += measure_time(binary_search, arr, target)

        # Compute average time for each search
        avg_time_linear = total_time_linear / iterations
        avg_time_binary = total_time_binary / iterations

        print(f"Size: {size}, Linear Search Avg Time: {avg_time_linear}, Binary Search Avg Time: {avg_time_binary}")

if __name__ == "__main__":
    main()
