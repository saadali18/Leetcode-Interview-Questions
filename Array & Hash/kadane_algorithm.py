# Problem link: https://leetcode.com/problems/maximum-subarray/
#  solution explanation: https://www.youtube.com/watch?v=AHZpyENo7k4&t=939s


# Solution 1:
# Complexity: O(n)

def maxSubArray(nums):
    maxSum = nums[0]
    sum = 0
    for item in nums:
        if sum < 0:
            sum = 0
        sum += item
        if sum>maxSum:
            maxSum=sum
        

    return maxSum



