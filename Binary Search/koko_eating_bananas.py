# Problem link: https://leetcode.com/problems/koko-eating-bananas
# Best solution explanation: https://www.youtube.com/watch?v=U2SozAs9RzA
# Medium Blog : https://medium.com/@umairazmatt/first-ever-leet-code-solution-by-umair-azmat-koko-eating-bananas-b18170bc9511

# Solution 1:
import math

class Solution:
    def minEatingSpeed(self, piles, h):
        # Set the initial search range for the eating speed
        left, right = 1, max(piles)

        # Perform binary search to find the minimum speed
        while left <= right:
            # Calculate the midpoint speed to test
            mid = (left + right) // 2
            
            # Calculate the total hours needed to finish at speed 'mid'
            total_hours = sum(math.ceil(pile / mid) for pile in piles)

            # If total hours are within the allowed hours, try a smaller speed
            if total_hours <= h:
                right = mid - 1  # Search for a smaller speed
            else:
                left = mid + 1  # Increase speed since current speed is too slow

        # Return the minimum speed found that allows Koko to finish in 'h' hours
        return left

# Complexity:
#Time Complexity: 𝑂(𝑛log(max(piles)))
#Space Complexity: 𝑂(1)