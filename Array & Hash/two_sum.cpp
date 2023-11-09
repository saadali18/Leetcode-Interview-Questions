// Problem Link: https://leetcode.com/problems/two-sum/
// Time Complexity O(n).

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {

        unordered_map<int, int> numSet;

        for (int i = 0; i < nums.size(); i++)
        {

            int complement = target - nums[i];

            // if pair found in the map
            if (numSet.find(complement) != numSet.end())
            {
                return {numSet[complement], i};
            }
            // Storing elements as key and its index as value
            numSet[nums[i]] = i;
        }

        return {};
    }
};