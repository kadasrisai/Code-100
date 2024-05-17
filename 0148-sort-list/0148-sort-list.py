# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        arr = []
        curr = head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
    
    # Step 2: Sort the list of values
        arr.sort()
    
    # Step 3: Traverse the linked list again and update the nodes with sorted values
        curr = head
        idx = 0
        while curr is not None:
            curr.val = arr[idx]
            idx += 1
            curr = curr.next
    
        return head
        