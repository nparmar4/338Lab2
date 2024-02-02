1. 
    - Adaptability to Uniformly Distributed Data:
        Binary search always examines the middle element in an array. On the other hand, interpolation search estimates the probable position of the target element based on its value and the distribution of values in the array.This adaptability allows it to converge to the target position more quickly when the data is evenly spread.

    - Variable Step Size:
        Interpolation search uses a variable step size, which adjusts its search space based on the values of the elements in an array. This kind of step size enables it to cover more efficiently when the values in the array are not evenly spaced. On the other hand, binary search will always divide the search space in half. This could not be optimal in certain cases.

2. 
Estimation Accuracy: 
    - Interpolation search utilizes a formula that assumes a linear relationship between indices and values in the given array. However, this assumption only works well when the data is evenly distributed. If the distribution is skewed, then the linear interpolation has a chance of not accurately representing the actual distribution. This can result in the estimated positions that are returned to be inaccurate. 

Convergence Speed:
    - Quick convergence of the search space to the target element is one major things that determines the effectiveness of interpolation search. If the data distribution is not uniform, then the interpolation search has a chance of not operating at the same level of efficiency. 

Potential for Overhead:
    - Due to the extra computation involved in the interpolatuon formula, there is a chance of overhead being produced when the assumptions regarding data distribution are not met. When the distribution is not uniform, the algorithm could spend extra time trying to recalculate positions and make necessary adjustments, which hinders overall efficency.

3. The part of the code that would be affected would be the one representing the interpolation formula:

        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

This part of the code makes a linear relationship assumption between the indices and values in the array. In order to adapt this search to a different distribution, an adjustment to this formula would need to be made to match the characterstics of the newer distribution. These adjustments will vary depending on the nature of the distribution that is used.

4. When the data is not sorted. Binary search and interpolation search assume that the data is sorted.

5. In the case of smaller datasets or when a target element is located near the starting point of an array. This is due to the constant time complexity of a linear search, which makes it more efficient in scenarios where the computational overhead of certain algorithms outweigh the benefits. Linear search is also better and preferred in cases where the target values in located near the starting point of the array. This helps to avoid overhead related to divided search spaces in binary and interpolation algorithms.

6. In order for binary and interpolation search algorithms to bypass the limitation on unsorted data, the simplest solution is to first sort the unsorted data. By sorting thr data first, it will enable the binary and interpolation searches to function as expected and correctly.

Sources used to research:
- https://www.geeksforgeeks.org/interpolation-search/
- https://www.geeksforgeeks.org/binary-search/
- https://www.geeksforgeeks.org/linear-search/ 

