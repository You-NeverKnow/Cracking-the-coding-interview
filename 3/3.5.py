# -----------------------------------------------------------------------------|
def main():
    """

    """

    stack = [11, 2, 3, 4, 5]
    print(sort_stack(stack))
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def sort_stack(stack: list) -> list:
    """

    """
    len_stack = len(stack)

    for i in range(len_stack - 1):
        largest = float("-inf")
        largest_set = False
        temp_stack = []

        for j in range(len_stack - i):
            item = stack.pop()
            if item > largest:
                if largest_set:
                    temp_stack.append(largest)
                largest = item
                largest_set = True
                continue
            temp_stack.append(item)

        stack.append(largest)

        while temp_stack:
            stack.append(temp_stack.pop())
    return stack
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
