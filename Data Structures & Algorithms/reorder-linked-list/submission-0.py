# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        print("length:", length)
        mid = length//2
        print("mid:", mid)
        index=0
        curr = head
        while index<mid:
            index+=1
            curr = curr.next
        print("curr_val", curr.val)
        temp = curr.next
        curr.next = None
        curr = temp
        # Reverse the second half
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr1 = head
        curr2 = prev
        while curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next=curr2
            curr1.next.next = temp1
            curr2=temp2
            curr1=temp1
            