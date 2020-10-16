#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        prev = None
        def reverse(prev, node):
            if not node: return prev
            _next = node.next
            node.next = prev
            return reverse(node, _next)
        return reverse(prev, head)
# @lc code=end

