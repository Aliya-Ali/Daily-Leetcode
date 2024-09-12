# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #first step we have find the midpoint of linklist
        dummy = ListNode(0, head)
        slow = head
        fast = head.next
        while fast and fast.next:
            slow =  slow.next
            fast = fast.next.next
        
        tmp  = slow.next
        slow.next= None
        
        #2 step: how to reverse the linklist
        
        prev = None
        second = tmp
        while second:
            front = second.next 
            second.next =  prev
            prev = second
            second = front
        
        # 3 step: merge the first linklist and reversed of second linklist
        
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next , second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1 , tmp2
        
        
        
        
        