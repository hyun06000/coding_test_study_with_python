from frame import Solution as frame


inputs = []
labels = []

# 1
class Solution(frame):
    def answer_method(self, head: ListNode) -> ListNode:
        def rev(cur_node, pre_node=None):
            if not cur_node:
                return pre_node
            next_node, cur_node.next = cur_node.next, pre_node
            return rev(next_node, cur_node)

        return rev(head)

sol = Solution(1)
sol.checker(inputs, labels)

