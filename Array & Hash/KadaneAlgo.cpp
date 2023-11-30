#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

// Problem Link: https://leetcode.com/problems/maximum-subarray/

class Solution
{
public:
    int maxSubArray1(vector<int> &nums) {   //Time Complexity: O(N)
        // Check if the array is empty
        if (nums.size() == 0) 
            return 0;
        int maxSum = nums[0]; // Initialize with the first element of the array
        int currSum = 0;

        // Iterate through each element in the array
        for (int n : nums) {
            // If the current sum becomes negative, reset it to zero (start a new sub array)
            if (currSum < 0)
                currSum = 0;

            // Update the current sum by adding the current element
            currSum += n;

            // Update the overall maximum sub array sum found so far
            maxSum = max(maxSum, currSum);
        }
        return maxSum;
    }

    int maxSubArray2(vector<int> &nums) {   //Time Complexity: O(N)
        // Get the size of the input array
        int n = nums.size();

        // Check if the array is empty
        if (n == 0) {
            return 0;
        }

        int current_sum = nums[0]; 
        int max_sum = nums[0];    

        // Iterate through the array starting from the second element (index 1)
        for (int i = 1; i < n; ++i) {
            // Update the current sum by choosing the maximum between the current element and the sum of the previous subarray ending at the previous position
            current_sum = max(nums[i], current_sum + nums[i]);

            // Update the overall maximum subarray sum found so far
            max_sum = max(max_sum, current_sum);
        }

        // Return the final result, which is the maximum subarray sum found throughout the array
        return max_sum;
    }
};
