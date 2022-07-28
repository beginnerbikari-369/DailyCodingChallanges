# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def len(self,head):
        length = 0
        temp = head
        while(temp):
            length+=1
            temp = temp.next
        print(length)
        return length
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = self.len(head)
        fp=head
        if fp.next is None:
            return None
        sp=fp.next
        count = 1
        while(sp):
            if length-n == 0:
                return head.next
            if length-n==count:
                fp.next = sp.next
                return head
            count+=1
            fp=fp.next
            sp= sp.next
        return head
            
            
            