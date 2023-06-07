# Data structures way of organizing our data

# Implement the bubble sort algorithm in Python and analyze its time complexity.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubble_sort(arr=3)                


# The bubble_sort function takes an input array arr and performs the bubble sort algorithm on it.
#  The outer loop iterates n-1 times, where n is the length of the array. In each iteration, the inner loop iterates n-1-i times, where i is the current iteration of the outer loop.

# In the inner loop, adjacent elements are compared, and if they are out of order, they are swapped. 
# This process is repeated until the largest element "bubbles up" to its correct position at the end of the array.
#  After each iteration of the outer loop, the largest element from the remaining unsorted elements is guaranteed to be placed correctly at the end.

# The time complexity of the bubble sort algorithm is as follows:
# Best case: O(n) - when the input array is already sorted, the algorithm only needs to perform a single pass through the array to verify that it is sorted.
# Average case: O(n^2) - the nested loops iterate over the array, comparing and swapping elements, resulting in quadratic time complexity.
# Worst case: O(n^2) - when the input array is sorted in reverse order, the algorithm needs to perform the maximum number of comparisons and swaps in each iteration.
# It's important to note that bubble sort is not considered an efficient sorting algorithm for large or nearly sorted arrays, as its time complexity is not optimal. Other sorting algorithms like quicksort or mergesort generally provide better performance.






