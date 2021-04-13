# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            pin = head.next
            head.next = self.swapPairs(pin.next)
            pin.next = head
            return pin
        return head