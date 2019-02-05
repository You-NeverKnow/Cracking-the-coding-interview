from BinNode import get_binary_tree, BinNode


# -----------------------------------------------------------------------------|
def main():
    """

    """

    sorted_array = sorted([1, 2, 5, 621, 23, 24, 4, 3, 2.1, 30, 31])
    # debug
    print("root = {}".format(sorted_array))
    
    root = get_binary_tree(sorted_array)
    # debug
    print("root = {}".format(root))
    root.left.left.right.right = BinNode(2.001)
    root.left.left.right.right._parent = root.left.left.right
    print((root.right.right.right))
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def next_order(node: BinNode) -> BinNode:
    """

    """

    if node.right:
        return smallest(node.right)
    else:
        return _up(node._parent, node)
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def _up(node: BinNode, right: BinNode) -> BinNode:
    """

    """
    if not node:
        return None

    if node.right != right:
        return node
    else:
        return _up(node._parent, node)
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def smallest(node: BinNode) -> BinNode:
    """

    """

    _smallest = node
    while node.left:
        _smallest = node.left
        node = node.left

    return _smallest
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
