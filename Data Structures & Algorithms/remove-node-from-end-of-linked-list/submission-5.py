# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = dummy, dummy
        index = 0
        while index < n:
            r = r.next
            index+=1
        while r and r.next:
            l=l.next
            r=r.next
        # print("l.val", l.val)
        l.next = l.next.next
        return dummy.next