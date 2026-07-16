# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        out=None
        tail=None
        while l1 and l2:
            if l1.val < l2.val:
                if out is None:
                    out = l1
                    tail = out
                else:
                    tail.next=l1
                    tail = tail.next
                l1=l1.next
            else:
                if out is None:
                    out = l2
                    tail = out
                else:
                    tail.next=l2
                    tail = tail.next
                l2=l2.next
        if l1:
            if out is None:
                out = l1
            else:
                tail.next=l1
        elif l2:
            if out is None:
                out = l2
            else:
                tail.next=l2
        return out
        