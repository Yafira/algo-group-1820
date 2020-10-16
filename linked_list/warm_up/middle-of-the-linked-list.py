#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
# @lc code=end
