# [83] Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        if current is None:
            return
        while current.next is not None:
            if current.val == current.next.val:
                new = current.next.next
                current.next = None
                current.next = new
            else:
                current = current.next

        return head
