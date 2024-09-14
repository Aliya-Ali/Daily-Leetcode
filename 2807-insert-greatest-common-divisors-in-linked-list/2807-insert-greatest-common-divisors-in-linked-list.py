# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            a = curr.val
            b = curr.next.val
            while b > 0:
                a , b = b , a %b
            
                
            temp = curr.next
            curr.next = ListNode(a, temp)
            curr = curr.next.next
        return head
            
        