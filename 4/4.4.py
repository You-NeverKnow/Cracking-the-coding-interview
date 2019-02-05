from BinNode import get_binary_tree, BinNode


# -----------------------------------------------------------------------------|
def main():
    """

    """

    sorted_array = sorted([1, 2, 5, 621, 23, 24])
    root = get_binary_tree(sorted_array)
    is_balanced_, depth = is_balanced(root)
    # debug
    print("is_balanced_ = {}".format(is_balanced_))

# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def is_balanced(node: BinNode) -> (bool, int):
    """

    """

    if not node:
        return True, 0

    left_balanced, left_len = is_balanced(node.left)
    right_balanced, right_len = is_balanced(node.right)
    length_node = 1 + max(left_len, right_len)

    if (not left_balanced) or (not right_balanced):
        return False, length_node

    return abs(left_len - right_len) <= 1, length_node
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
