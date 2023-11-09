// Problem link : https: // leetcode.com/problems/maximum-product-subarray/
// Solution link : https://www.youtube.com/watch?si=WJ4Lb92yGLDT1Xev&v=HCL4_bOd3-4&feature=youtu.be

// Soluion 1
// time complexity is O(n)

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
        return maxSum;
    }