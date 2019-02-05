# -----------------------------------------------------------------------------|
def main():
    """

    """

    # Using data structure: hashset
    a = is_unique1(input())

    # Without using data structure: sorting
    b = is_unique2(input())

    # debug
    print("a, b = {}, {}".format(a, b))

# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def is_unique1(input_string):
    """

    """
    chars = set()

    for char in input_string:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def is_unique2(input_string):
    """

    """

    sorted_input = sorted(input_string)
    for i, ch in enumerate(sorted_input):
        if i != len(sorted_input) - 1 and ch == sorted_input[i+1]:
                return False

    return True
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
