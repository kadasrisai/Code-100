# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        
        # Compute the length of the list
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        
        # Connect the tail to the head to make it a circular list
        tail = temp
        tail.next = head
        
        # Find the new tail, which is (length - k % length - 1)th node
        k = k % length
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # The new head is the next node of the new tail
        new_head = new_tail.next
        new_tail.next = None  # Break the cycle
        
        return new_head
        