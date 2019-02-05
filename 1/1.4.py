import sys
from collections import Counter


# -----------------------------------------------------------------------------|


def main():
    """

    """

    print(permutation_palindrome(sys.argv[1]))
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def permutation_palindrome(str_in):
    """

    """

    str_in = "".join(str_in.split())
    char_counter = Counter(str_in)

    middle_set = False
    for ch, count in char_counter.items():
        if count % 2 != 0:

            if not middle_set:
                middle_set = True
            else:
                return False

    return True

# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
