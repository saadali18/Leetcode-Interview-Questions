# Problem link: https://leetcode.com/problems/3sum/

# Solution 1:
# Complexity: O(n^2)

def threeSum(nums):
    # Loop through an array and perform 2Sum algo inside the loop this way we can do it
    # in O(N^2)
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        num_set = set()

        for j in range(i + 1, n):
            complement = target - nums[j]

            if complement in num_set:
                new_set = [nums[i], complement, nums[j]]
                if new_set not in result:
                    result.append(new_set)
                    while j < n - 1 and nums[j] == nums[j + 1]:
                        j += 1

            num_set.add(nums[j])

    return result
