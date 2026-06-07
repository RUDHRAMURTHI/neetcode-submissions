# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)
            prev = head
            curr = head.next
            curr.next = prev
        head.next =None
        return newhead
        