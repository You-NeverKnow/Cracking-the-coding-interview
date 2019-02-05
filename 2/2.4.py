from Node import Node


# -----------------------------------------------------------------------------|
def main():
    """

    """

    _list = Node().init_from_list([1, 2, 7, 8, 5, 4])
    print(partition(_list, 5).linked_list_to_list())
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def partition(head: Node, p: int) -> Node:
    """

    """

    dummy_left = Node()
    left = dummy_left
    dummy_right = Node()
    right = dummy_right

    while head:
        if head.value < p:
            left.next_node = head
            left = left.next_node
        else:
            right.next_node = head
            right = right.next_node

        head = head.next_node

    right.next_node = None
    left.next_node = dummy_right.next_node

    return dummy_left.next_node
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()