// Sidra Sonia Aziz
// Problem: https://leetcode.com/problems/reverse-linked-list/
// Time Complexity: O(n)
// Solution:
class Solution {
public:
   public:
    ListNode* reverseList(ListNode* head) {
        if(head==nullptr || head->next==nullptr){
            return head;
        }
        ListNode* newHead = reverseList(head->next);
        ListNode* headNext = head->next;
        headNext->next = head;
        head->next = NULL;
        return newHead;
    }
};