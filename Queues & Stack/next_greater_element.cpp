//Problem Link : https://leetcode.com/problems/next-greater-element-i/description/
//Solution Link:https://youtu.be/V5r7PQhcJCQ?si=yoUawrOUbBs5AuVJ
//Complexity: O(N)

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    vector <int> nge;
    stack<int> st;
    unordered_map<int,int>map;
    for (int i = 0; i < nums2.size(); i++)
    {
        while((! st.empty())  && (nums2[i]>nums2[st.top()])){
            map[nums2[st.top()]] = nums2[i];
            st.pop();
        }
        st.push(i);
    }
    while(! st.empty()){
        map[nums2[st.top()]] = -1;
        st.pop();
    }
    for(int i=0;i<nums1.size();i++){
        nge.push_back(map[nums1[i]]);
    }
    return nge;   
    }
};