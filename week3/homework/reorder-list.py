# https: // leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        temp = []
        current = head

        while current:
            temp.append(current)
            current = current.next

        n = len(temp)
        for i in range(n // 2):
            temp[i].next = temp[n - 1 - i]
            temp[n - 1 - i].next = temp[i + 1]

        temp[n // 2].next = None
