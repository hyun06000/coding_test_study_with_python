class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def link_to(self, node):
        self.next = node


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.link_to(two)
two.link_to(three)

while one.next is not None:
    print(one.val)
    one = one.next


def make_list_node(input_list: list) -> ListNode:
    for i, n in enumerate(input_list):
        input_list[i] = ListNode(n)
    for i in range(len(input_list)-1):
        input_list[i].link_to(input_list[i + 1])
    input_list[-1].link_to(None)
    return input_list[0]

list_node = make_list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])

while list_node.next is not None:
    print(list_node.val)
    list_node = list_node.next
