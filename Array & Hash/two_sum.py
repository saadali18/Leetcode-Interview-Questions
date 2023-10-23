# Problem link: https://leetcode.com/problems/two-sum/

# Solution 1:
# Complexity: O(n)

def twoSum(nums, target):
    # a + b  =  target
    # a = target - b
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i]

        num_indices[num] = i

    return []