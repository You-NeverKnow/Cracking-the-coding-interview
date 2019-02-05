from Node import Node


# -----------------------------------------------------------------------------|
def main():
    """

    """

    _list1 = Node().init_from_list([1, 2, 3])
    _list2 = Node().init_from_list([9, 9, 2, 1])
    # debug
    print("123 + 921 = {}".format(123 + 9921))
    #
    # print(reverse(add(_list1, _list2)).linked_list_to_list())
    # print(pad(_list1, 5).linked_list_to_list())
    print(recursive_add(_list1, _list2).linked_list_to_list())
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def recursive_add(_list1: Node, _list2: Node) -> Node:
    """
    Adds two linked lists numbers without reversing them
    """

    l1 = len(_list1)
    l2 = len(_list2)

    if l1 > l2:
        _list2 = pad(_list2, l1-l2)
    else:
        _list1 = pad(_list1, l2-l1) # exec

    partial_sum_node, carry = _add(_list1, _list2)

    if carry == 1:
        return Node(1, partial_sum_node)
    else:
        return partial_sum_node

# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def pad(_list: Node, count) -> Node:
    """
    Pads a linked list with zeroes
    """

    zero_node = Node()
    current = zero_node
    while count > 0:
        current.next_node = Node(0)
        current = current.next_node
        count -= 1

    current.next_node = _list
    return zero_node.next_node
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def _add(_list1: Node, _list2: Node) -> (Node, int):
    """

    """
    if not _list1 and not _list2:
        return None, 0

    partial_sum_node, carry = _add(_list1.next_node, _list2.next_node)

    value = _list2.value + _list1.value + carry # 10
    sum_node = Node(value % 10, partial_sum_node) # (0, None), 1

    return sum_node, value // 10
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def add(_list1: Node, _list2: Node) -> Node:
    """

    """

    carry = 0

    if len(_list1) > len(_list2):
        longer = _list1
        shorter = _list2
    else:
        longer = _list2
        shorter = _list1
        
    list_sum = Node()
    current = list_sum

    while shorter:
        value = carry + shorter.value + longer.value

        current.next_node = Node(value % 10)
        current = current.next_node
        carry = value // 10

        shorter = shorter.next_node
        longer = longer.next_node

    if longer:
        value = carry + longer.value
        longer.value = value % 10
        carry = value // 10
        current.next_node = longer
        current = current.next_node

    if carry == 1:
        current.next_node = Node(1)

    return list_sum.next_node
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def reverse(head: Node) -> Node:
    """

    """

    if not head:
        return head

    previous = None
    current = head

    while current:
        next_node = current.next_node
        current.next_node = previous

        previous = current
        current = next_node

    return previous
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
