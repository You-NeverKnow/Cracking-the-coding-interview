from Node import Node


# -----------------------------------------------------------------------------|
def main():
    """

    """
    head = Node().init_from_list([1, 1, 2])
    delete_duplicates(head)
    print(head.linked_list_to_list())
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def delete_duplicates(head: Node):
    """
    Deletes duplicates from a linked list
    """

    if head is None:
        return head

    _set = set()
    previous = head
    current = previous.next_node
    _set.add(head.value)

    while current:
        if current.value in _set:
            previous.next_node = current.next_node
        else:
            previous = current
            _set.add(current.value)
        current = current.next_node
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
