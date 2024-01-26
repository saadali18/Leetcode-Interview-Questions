class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = []

        for num in nums1:
            found = False
            for i in range(len(nums2)):
                if found and num < nums2[i]:
                    ans.append(nums2[i])
                    break
                if nums2[i]==num:
                    found= True
            else:
                ans.append(-1)

        return ans
