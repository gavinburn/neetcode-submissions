class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        counter = head
        count=0
        while counter:
            counter=counter.next
            count+=1
        
        split = count // 2
        if split < 1: return
        count=0

        counter = head

        while count <split:
            prev = counter
            counter=counter.next
            count+=1

        reversedHead = sortList(counter)
        prev.next=None
        counter = head
        count=0

        while counter:
            l1 = counter.next
            l2=reversedHead.next
            counter.next=reversedHead
            count+=1
            if count ==split: 
                break
            reversedHead.next = l1
            counter=l1
            reversedHead=l2
            

        return


def sortList(head) -> ListNode:
    curr=None
    while head:
        nextNode = head.next
        head.next = curr
        curr=head
        head=nextNode

    return curr
