# Problem link: https://leetcode.com/problems/maximum-product-subarray/
# Best solution explanation: https://www.youtube.com/watch?v=lXVy6YWFcRM

# Solution 1:
# Complexity: O(n)

def maxProduct(nums):
    maxProd = max(nums)
    curMin, curMax = 1, 1
    for n in nums:
        if n == 0:
            curMax, curMin = 1, 1
            continue
        preMax = curMax
        curMax = max(curMin * n, curMax * n, n)
        curMin = min(curMin * n, preMax * n, n)
        maxProd = max(maxProd, curMax)

    return maxProd
