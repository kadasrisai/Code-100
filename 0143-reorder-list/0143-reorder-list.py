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
        current = head
        p1 = head
        p2 = head
        values = []
        while p2:
            values.append(p2.val)
            p2 = p2.next
        left, right = 0, len(values) - 1
        
        while left <= right:
            p1.val = values[left]
            p1 = p1.next
            if p1 is not None:
                p1.val = values[right]
                p1 = p1.next
            left += 1
            right -= 1
        