
"""
1. This code is a recursive function that is used to calculate the nth Fibonacci number. 
   However, this method is not a very good implementation.
2. No, this is not a divide and conquer algorithm. Although it uses recursion to break down the code, 
   each function call overlaps and recomputes a number from the previous call.
3. The time complexity for this algorithm is O(2^n). This is because for each recursive call, 
   two more recursive calls are made, sp it grows exponentially with base 2.
5. The complexity of the fibonacci function with memoization is O(n). This is because each Fibonacci number 
   is calculated only once and stored in the parameters a and b for n recursive calls.
"""

import timeit
import numpy as np
import matplotlib.pyplot as plt

#Provided code
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
# 4:Optimized code
def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fibonacci(n-1, b, a+b)

# 6:Timing and Plotting
original_times_list = []
improved_times_list = []

for n in range(0,36):
    original_time = timeit.timeit(lambda: func(n), number=1)
    original_times_list.append(original_time)

    improved_time = timeit.timeit(lambda:fibonacci(n), number=1)
    improved_times_list.append(improved_time)

plt.plot(range(36), original_times_list, label='Original')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Execution Time for Original Fibonacci')
plt.savefig('ex1.6.1.jpg')
plt.show()

plt.plot(range(36), improved_times_list, label='Optimized')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Execution Time for Improved Fibonacci')
plt.savefig('ex1.6.2.jpg')
plt.show()
