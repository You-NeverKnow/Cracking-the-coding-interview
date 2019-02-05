from BinNode import get_binary_tree, BinNode


# -----------------------------------------------------------------------------|
def main():
    """

    """

    sorted_array = sorted([1, 2, 3, 4, 5, 6])
    root = get_binary_tree(sorted_array)
    print(get_combo([root]))
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def get_combo(leaves: list) -> list:
    """

    """
    if not leaves:
        return []

    combos = []
    for new_root in leaves:
        new_leaves = leaves[:]
        new_leaves.remove(new_root)
        if new_root.right:
            new_leaves.append(new_root.right)
        if new_root.left:
            new_leaves.append(new_root.left)

        _combos = get_combo(new_leaves)

        if _combos:
            for _combo in _combos:
                combos.append([new_root] + _combo)
        else:
            combos.append([new_root])
    return combos
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
