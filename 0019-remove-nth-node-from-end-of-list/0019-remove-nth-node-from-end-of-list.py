# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        q = head
        length = 0
        
        if(head.next==None):
            return None
        
        while(p.next != None):
            length+=1
            p = p.next
        if(length - n < 0):
            head = head.next
        else:
            for i in range(length-n):
                q = q.next
       
            q.next = q.next.next
        
        return head
        
        
            
            
            
        