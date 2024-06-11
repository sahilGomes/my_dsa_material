# Sliding window
It ensures that each value is only visited at most twice and the time complexity is still O(n).

# There are basically two types of sliding window([link](https://www.geeksforgeeks.org/window-sliding-technique/)):
1. Fixed size sliding window
    - Find the size of the window required, say K.
    - Compute the result for 1st window, i.e. include the first K elements of the data structure.
    - Then use a loop to slide the window by 1 and keep computing the result window by window.

2. Variable Size Sliding Window:
    - In this type of sliding window problem, we increase our right pointer one by one till our condition is true.
    - At any step if our condition for left pointer shrink satisfies, we shrink the size of our window by increasing left pointer.
    - Again, when our condition false for left pointer, we start increasing the right pointer and follow step 1.
    - We follow these steps until we reach to the end of the array.