# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Find length of the list
        length=0
        curr = head
        while curr:
            length+=1
            curr=curr.next
        # print("length:", length)
        if length == 1:
            return None
        pos = length-n
        # print("pos:", pos)
        if pos == 0:
            return head.next
        index =1
        prev = head
        while index < pos:
            index+=1
            prev = prev.next
        # print("prev.val", prev.val)
        if prev.next:
            temp = prev.next
            prev.next =prev.next.next
            temp.next = None
        return head

        