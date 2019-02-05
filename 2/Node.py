# =============================================================================|
class Node:
    """
    Defines a node for linked list
    """
    # -------------------------------------------------------------------------|
    def __init__(self, value: int = None, next_node = None):
        """
        Constructor for Node
        """
        self.value = value
        self.next_node = next_node
    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|

    def __len__(self,):
        """

        """

        length = 1
        current = self

        while current.next_node:
            length += 1
            current = current.next_node

        return length
    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|
    def init_from_list(self, linked_list: list):
        """

        """

        dummy_head = Node()
        current = dummy_head
        for item in linked_list:
            current.next_node = Node(value = item)
            current = current.next_node

        if not linked_list:
            return dummy_head
        return dummy_head.next_node
    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|
    def linked_list_to_list(self) -> list:
        """

        """

        if self.value is None and self.next_node is None:
            return []

        current = self
        _list = []
        while current.next_node:
            _list.append(current.value)
            current = current.next_node

        _list.append(current.value)
        return _list
    # -------------------------------------------------------------------------|
# =============================================================================|
