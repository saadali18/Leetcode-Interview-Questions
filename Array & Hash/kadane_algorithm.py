# Problem link: https://leetcode.com/problems/maximum-subarray/
# Best solution explanation: https://www.youtube.com/watch?v=5WZl3MMT0Eg

# Solution 1:
# Complexity: O(n)

def maxSubArray(nums):
    maxSum = nums[0]
    currentSum = 0
    for n in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += n
        maxSum = max(maxSum, currentSum)

    return maxSum
