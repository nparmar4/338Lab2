import timeit
import cProfile
import re

def sub_function(n):
        #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

cProfile.run('re.compile("sub_function, test_fuction,third_function")')

"""
1. What is a profiler, and what does it do? [0.25 pts]
    A profiler module that provides a deterministic profiling of a python program. This profile os full of tatistics that describ how often certain parts of the program are executed and how long they are executed for. 

2. How does profiling differs from benchmarking? [0.25 pts]
    Benchmarking is concerned with the overall perfomance of a program or piece of code, while profiling 
    looks at smaller parts of the code and reveals which function takes up the most execution time.     

3. Use a profiler to measure execution time of the program (skip function definitions) [0.25 pt]
    Added the following line to the code: cProfile.run('re.compile("sub_function, test_fuction,third_function")')

4. Discuss a sample output. Where does execution time go? [0.25 pts]
    A sample output looks like the following (but much longer): 
    
        69 function calls (24 primitive calls) in 68.742 seconds

        Ordered by: standard name

        ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                1    0.000    0.000    0.000    0.000 ex3.py:11(test_function) 
                1    0.000    0.000   68.741   68.741 ex3.py:17(third_function)
                1   68.741   68.741   68.741   68.741 ex3.py:19(<listcomp>)    
                55/10    0.000    0.000    0.000    0.000 ex3.py:4(sub_function)   
                10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
                1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    
    The total execution time is in the first line, next to the number of function calls. 

"""