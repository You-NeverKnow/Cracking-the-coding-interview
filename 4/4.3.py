from BinNode import get_binary_tree, BinNode


# -----------------------------------------------------------------------------|
def main():
    """

    """

    sorted_array = sorted([1, 2, 3, 5, 621, 81, 23])
    root = get_binary_tree(sorted_array)
    print(root)

    print(linked_list_depth(root))
    print(linked_list_depth2(root))
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def linked_list_depth2(root: BinNode) -> list:
    """

    """

    list_of_depths = []
    current_list = [root]

    while current_list:
        list_of_depths.append(current_list)
        parents = list_of_depths[-1]
        current_list = []

        for parent in parents:
            if parent.left:
                current_list.append(parent.left)
            if parent.right:
                current_list.append(parent.right)

    return [(i, node.value) for i, l in enumerate(list_of_depths) for node in l]
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def linked_list_depth(root: BinNode) -> list:
    """

    """

    queue = [(root, 0)]
    list_of_depths = []
    current_depth = -1

    while queue:
        item, depth = queue.pop(0)

        if current_depth != depth:
            list_of_depths.append([])
            current_depth = depth

        list_of_depths[-1].append(item.value)

        if item.left:
            queue.append((item.left, depth+1))
        if item.right:
            queue.append((item.right, depth+1))

    return list_of_depths
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
