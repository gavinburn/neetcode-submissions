# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prevSet = set()

        curr = head
        output = False

        while curr:
            if curr:
                if curr in prevSet: 
                    output = True
                    break
                prevSet.add(curr)
                curr=curr.next
            else:
                break

        return output