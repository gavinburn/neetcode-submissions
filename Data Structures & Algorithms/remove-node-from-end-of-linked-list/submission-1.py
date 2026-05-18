# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr=head
        total=0

        while curr:
            curr=curr.next
            total+=1

        count=0
        curr = head

        target = total-n

        prev=None
        nextNode=None

        while count < target:
            prev=curr
            curr = curr.next
            nextNode=curr.next
            count+=1


        if prev:
            prev.next=nextNode
            curr.next=None
        else:
            head=curr.next
        

        return head

        