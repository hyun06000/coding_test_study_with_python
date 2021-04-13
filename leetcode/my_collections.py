class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def make_list_node(input_list: list):
    for i, n in enumerate(input_list):
        input_list[i] = ListNode(n)
    for i in range(len(input_list)-1):
        input_list[i].next = input_list[i + 1]
    input_list[-1].next = None
    return input_list[0]

def ln_to_list(input_list: list):
    result = []
    while input_list:
        result.append(input_list.val)
        input_list = input_list.next
    return result

def print_list_node(input_list: list):
    result = []
    while input_list:
        result.append(input_list.val)
        input_list = input_list.next
    print(result)