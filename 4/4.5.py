from BinNode import get_binary_tree, BinNode


# -----------------------------------------------------------------------------|
def main():
    """

    """

    sorted_array = sorted([1, 2, 5, 621, 23, 24, 4])
    root = get_binary_tree(sorted_array)
    print("is_bst = {}".format(is_bst(root)))
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def is_bst(root: BinNode) -> bool:
    """

    """

    return _is_bst(root, (float("-inf"), float("inf")))
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def _is_bst(root: BinNode, bounds: (float, float)) -> bool:
    """

    """

    if not root:
        return True

    lower_bound, upper_bound = bounds
    self_valid = lower_bound < root.value < upper_bound
    left_valid = _is_bst(root.left, (lower_bound, root.value))
    right_valid = _is_bst(root.right, (root.value, upper_bound))

    return self_valid and left_valid and right_valid
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
