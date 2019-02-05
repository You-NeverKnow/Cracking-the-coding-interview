# =============================================================================|
class QueueWithStacks:
    """
    Implements a Queue data structure with two stacks
    """
    # -------------------------------------------------------------------------|
    def __init__(self):
        """
        Constructor for QueueWithStacks
        """
        self.push_stack = []
        self.pop_stack = []
    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|
    def pop(self):
        """

        """
        if not self.pop_stack:
            self._get_items_from_push_stack()

        return self.pop_stack.pop()
    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|
    def push(self, item):
        """

        """
        self.push_stack.append(item)
    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|
    def _get_items_from_push_stack(self):
        """

        """

        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
    # -------------------------------------------------------------------------|
# =============================================================================|


# -----------------------------------------------------------------------------|
def main():
    """

    """

    queue = QueueWithStacks()
    queue.push(5)
    queue.push(15)
    queue.push(50)

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())

    queue.push(5)
    queue.push(15)
    queue.push(50)

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())

# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
