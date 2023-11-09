
// Problem Link : https://leetcode.com/problems/maximum-subarray/
// Time Complexity: O(n).

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int sum = 0;
        int maxi = nums[0];

        for (int i = 0; i < nums.size(); i++)
        {

            sum += nums[i];
            maxi = max(maxi, sum);

            if (sum < 0)
            {
                sum = 0;
            }
        }
        return maxi;
    }
};

// solution 2
//  solution link : https://youtu.be/HCL4_bOd3-4?si=WJ4Lb92yGLDT1Xev

#include <iostream>
#include <vector>

using namespace std;

int maxSubArray(vector<int> &nums)
{
    int maxSum = nums[0];
    int currentSum = 0;

    for (int item : nums)
    {
        if (currentSum < 0)
        {
            currentSum = 0;
        }
        currentSum += item;

        if (currentSum > maxSum)
        {
            maxSum = currentSum;
        }
    }

    return maxSum;
}