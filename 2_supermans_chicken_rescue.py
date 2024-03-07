"""
To simplify the problem, let's convert the problem into an abstract representation
that is easier for our brain to work with.
Imagine we have an infinitely long number line which represents the 1D world
that chickens are living in. Each chicken is represented by a dot on this line.
The roof is simply a short line segment that we will try to slide around the
number line to cover as many dots as possible.

As we slide the line segment from left to right, we will keep track of the number of
dots that the segment covers at each instance in time. And we will also keep track
of the maximum number of dots that the line segment can cover so far.

How can we find the number of dots that the line segment can cover at any specific
range on the number line?
1. The naive bruteforce approach is to iterate through all the dots on the line
  and check if the line segment intersects with the dot. This is O(n) time complexity.
2. We can use a binary search to find the number of dots that the line segment can
  cover at any specific range. This requires a sorted list. We do it by finding
  the dots on the left and right corner of the line segment and query their indices.
  The subtraction of the two indices gives us the number of dots that the line
  segment can cover. This is O(log n) time complexity.

The 2nd approach is more efficient than the 1st approach therefore we will use it
to solve the problem. In the problem statement, we are given a list that is already
sorted in ascending order. This means we don't have to sort the list again.

So here is the solution:
We will iterate through the list doing these steps to each dot in the list:
1. Treat the dot as the leftmost point for the line segment
2. Perform binary search to find the rightmost dot that the line segment can cover
3. Count the number of dots that the line segment can cover from the leftmost dot
   to the rightmost dot
4. We will keep track of the maximum number so far

Time complexity analysis:
Iteration is O(n) time complexity and binary search is O(log n) time complexity.
This means the overall time complexity is O(n log n).

Memory complexity analysis:
We do not store any additional data other than the maximum number of dots that
the line segment can cover. This means the memory complexity is O(1).
"""

import bisect


def count_segment_coverage(dots, start_index, segment_length):
    """Given a list of dots, an index of the starting dot, and a segment length,
    return the number of dots that the line segment can cover from the starting
    dot to the end of the segment.
    """
    left_position = dots[start_index]
    right_position = left_position + segment_length

    # Let's say that we are trying to find number 5 in a list.
    # There are 3 interesting cases to think about:
    # 1. The number 5 exists once e.g. [2, 3, 5, 7, 9]
    # 2. The number 5 exists multiple times e.g. [2, 3, 5, 5, 5, 7, 9]
    # 3. The number 5 does not exist e.g. [2, 3, 7, 9]
    # In all cases, it would be helpful to find the index of the number 7 in the
    # list. Fortunately, bisect_right() function provides this functionality.
    end_index = bisect.bisect_right(dots, right_position)

    return end_index - start_index


if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    dots = [int(x) for x in input().split()]

    # In the original problem, roof length of 1 is the same as segment length of
    # 0 in my solution. So we will subtract 1 from the input k to make it
    # work with my solution.
    k -= 1

    max_coverage = 0
    for i in range(n):
        # in a situation where we have several dots on the same position, we
        # will check for coverage only starting from the first dot
        if i > 0 and dots[i] == dots[i - 1]:
            continue

        coverage = count_segment_coverage(dots, i, k)
        max_coverage = max(max_coverage, coverage)

    print(max_coverage)
