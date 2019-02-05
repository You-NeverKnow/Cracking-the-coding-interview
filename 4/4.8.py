from BinNode import get_binary_tree, BinNode


# -----------------------------------------------------------------------------|
def main():
    """

    """

    sorted_array = sorted([1, 2, 5, 621, 23, 24])
    root = get_binary_tree(sorted_array)

# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def common_ancestor(root: BinNode, node1: BinNode, node2: BinNode) -> BinNode:
    """

    """

    stack = [root]
    min_len = 1
    common = root
    nodes_to_find = {node1, node2}

    while stack:

        if stack[-1] in nodes_to_find:
            nodes_to_find.remove(stack[-1])
            if len(nodes_to_find) == 0:
                return common
            min_len = len(stack)
            common = stack[-1]

        if len(stack) < min_len:
            common = stack[-1]
            min_len = len(stack)

        current = stack.pop()
        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
