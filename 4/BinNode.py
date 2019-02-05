# =============================================================================|
class BinNode:
    """

    """
    # -------------------------------------------------------------------------|
    def __init__(self, value, left = None, right = None):
        """
        Constructor for Node
        """

        self.value = value
        self.left = left
        self.right = right
        self._parent = None
        self.dict_repr = {self.value: [str(self.left), str(self.right)]}
    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|
    def __str__(self):
        """

        """
        return str(self.dict_repr)
    # -------------------------------------------------------------------------|

    def __repr__(self):
        return str(self.value)
# =============================================================================|


# -----------------------------------------------------------------------------|
def get_binary_tree(array: list) -> BinNode:
    """

    """
    return _get_binary_tree(array, 0, len(array)-1)
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def _get_binary_tree(array: list, start: int, end: int) -> BinNode:
    """

    """
    if start > end:
        return None

    mid = (end + start) // 2

    left = _get_binary_tree(array, start, mid-1)
    right = _get_binary_tree(array, mid+1, end)

    node = BinNode(value = array[mid], left = left, right = right)
    if left:
        left._parent = node
    if right:
        right._parent = node

    return node
# -----------------------------------------------------------------------------|

