from frame import Solution as frame
import collections

inputs = []
labels = []

# 1
Deque = collections.deque()

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(frame):
    def answer_method(self, head: ListNode) -> bool:
        if not head:
            return True

        q: Deque = collections.deque()

        while head is not None:
            q.append(head.val)
            head = head.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True


sol = Solution(1)
sol.checker(inputs, labels)





