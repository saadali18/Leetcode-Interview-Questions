
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