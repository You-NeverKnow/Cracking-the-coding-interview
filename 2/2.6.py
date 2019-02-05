from Node import Node


# -----------------------------------------------------------------------------|
def main():
    """

    """

    _list = Node().init_from_list(list("CAS"))
    print(is_palindrome_recursive(_list))
    print(is_palindrome_stack(_list))
    print(is_palindrome(_list))
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def is_palindrome_recursive(head: Node) -> bool:
    """

    """
    if not head:
        return True
    _, is_palindrome_ = _is_palindrome(head, len(head))
    return is_palindrome_
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def _is_palindrome(head: Node, length: int) -> (Node, bool):
    """

    """
    if length == 1:
        return head.next_node, True
    elif length == 2:
        return head.next_node.next_node, head.value == head.next_node.value

    next_node, is_palindrome_ = _is_palindrome(head.next_node, length - 2)

    return next_node.next_node, is_palindrome_ and head.value == next_node.value

# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def is_palindrome_stack(head: Node) -> bool:
    """

    """

    stack = []
    dummy_head = Node(next_node = head)
    fast = dummy_head
    slow = dummy_head

    while fast.next_node:
        slow = slow.next_node
        fast = fast.next_node
        if fast.next_node:
            fast = fast.next_node

    slow = slow.next_node
    while slow:
        stack.append(slow.value)
        slow = slow.next_node

    comparator = dummy_head.next_node
    while stack:
        if comparator.value != stack.pop():
            return False
        comparator = comparator.next_node

    return True
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def is_palindrome(head: Node) -> bool:
    """

    """

    if not head:
        return True

    reverse_list = reverse(deep_copy_linked_list(head))
    
    while head and reverse_list:
        if head.value != reverse_list.value:
            return False
        head = head.next_node
        reverse_list = reverse_list.next_node

    return True
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def deep_copy_linked_list(head: Node) -> Node:
    """

    """

    dummy = Node()
    list_copy = dummy
    while head:
        list_copy.next_node = Node(head.value)
        head = head.next_node
        list_copy = list_copy.next_node
    
    return dummy.next_node

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
