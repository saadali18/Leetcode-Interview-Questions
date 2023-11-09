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


# Solution 2:
# Complexity: O(n)

def max_sub_array( nums):
    current_sum = nums[0]
    max_sum = current_sum
    for i in range(1, len(nums)):
        current_sum = max(nums[i] + current_sum, nums[i])
        max_sum = max(current_sum, max_sum)
    return max_sum