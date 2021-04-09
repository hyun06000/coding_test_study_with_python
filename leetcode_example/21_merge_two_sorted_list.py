# 21_merge_two_sorted_list.py

from frame import Solution as frame
from my_collections import ListNode
from my_collections import make_list_node, ln_to_list, print_list_node

ListNode = ListNode()

input_1 = make_list_node([1, 2, 4])
input_2 = make_list_node([1, 3, 4])
label = make_list_node([1, 1, 2, 3, 4, 4])

# 1
class Solution(frame):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            if (not l1) or (l2 and l1.val > l2.val):
                l1, l2 = l2, l1
            if l1:
                l1.next = self.mergeTwoLists(l1.next, l2)

            return l1

sol = Solution(1)
re = sol.mergeTwoLists(input_1, input_2)

print_list_node(re)
print_list_node(label)