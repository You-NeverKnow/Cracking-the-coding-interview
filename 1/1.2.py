import sys
from collections import Counter


# -----------------------------------------------------------------------------|
def main():
    """

    """

    input_str1 = sys.argv[1]
    input_str2 = sys.argv[2]

    a = check_permutation(input_str1, input_str2)

    # debug
    print("{}".format(a))

# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def check_permutation(str1, str2):
    """

    """

    str1_chars = Counter(str1)
    str2_chars = Counter(str2)

    return str1_chars == str2_chars
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
