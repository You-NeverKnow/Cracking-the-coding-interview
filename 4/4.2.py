from BinNode import get_binary_tree


# -----------------------------------------------------------------------------|
def main():
    """

    """

    sorted_array = sorted([1, 2, 5, 621, 623])
    root = get_binary_tree(sorted_array)
    print(root)
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
