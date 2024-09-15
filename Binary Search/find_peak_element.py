# Problem link: https://leetcode.com/problems/find-peak-element
# Best solution explanation: https://www.youtube.com/watch?v=kMzJy9es7Hc

# Solution 1:
# Complexity: O(Log(n))

def findPeakElement(nums):
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare the middle element with its neighbors
        if nums[mid] > nums[mid + 1]:
            # If the mid element is greater than the next element, move left
            right = mid
        else:
            # If the mid element is less than the next element, move right
            left = mid + 1

    # When left and right pointers meet, we have found the peak element
    return left
