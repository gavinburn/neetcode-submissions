# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = l1
        head2 = l2

        curr1 = head1
        curr2 = head2


        carry = 0

        while curr1 or curr2:
            if curr1 and curr2:
                prev1=curr1
                prev2=curr2
                nextVal = curr1.val + curr2.val + carry
            elif curr1:
                # print("hit")
                # print(curr1.val, carry)
                prev1=curr1
                nextVal = curr1.val + carry
            else:
                prev2=curr2
                nextVal = curr2.val + carry

            if nextVal - 10 >= 0:
                carry = 1
                nextVal = nextVal - 10
            else: 
                carry = 0


            if curr1:
                curr1.val = nextVal
                curr1 = curr1.next
            else:
                # print("was it this")
                prev1.next = ListNode(nextVal, None)
                prev1 = prev1.next

            if curr2:
                # print("this should also happen")
                curr2 = curr2.next
        
        
        
        if carry ==1:
            prev1.next = ListNode(carry, None)



        return head1
        