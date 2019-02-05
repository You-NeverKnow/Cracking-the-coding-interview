from Node import Node


# -----------------------------------------------------------------------------|
def main():
    """

    """

    _list = Node().init_from_list([1, 2, 3, 4, 5])
    print(kth_element(_list, 2).value)
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def kth_element(head: Node, k: int) -> Node:
    """
    Returns kth element of a linked list
    """

    fast = head
    while k != 0:
        fast = fast.next_node
        k -= 1

    slow = head
    while fast.next_node is not None:
        slow = slow.next_node
        fast = fast.next_node

    return slow
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
