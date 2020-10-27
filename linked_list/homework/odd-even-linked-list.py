# [328] Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            odd, current = head, head.next

            while current and current.next:
                even = odd.next
                odd.next = current.next

                odd = odd.next
                current.next = odd.next

                odd.next = even
                current = current.next

        return head
