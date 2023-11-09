class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {

        unordered_map<int, int> numSet;

        for (int i = 0; i < nums.size(); i++)
        {

            int complement = target - nums[i];

            // if found in the map
            if (numSet.find(complement) != numSet.end())
            {
                return {numSet[complement], i};
            }

            numSet[nums[i]] = i;
            continue;
        }

        return {};
    }
};