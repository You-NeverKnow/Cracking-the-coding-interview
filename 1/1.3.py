import sys


# -----------------------------------------------------------------------------|
def main():
    """

    """
    url = sys.argv[1]
    length = sys.argv[2]

    # Pythonic
    a = "%20".join(url.split())
    print(a, len(a))

    # Imperative style
    url = list(url)
    i = len(url) - 1
    last_index = int(length) - 1

    while i != 0:
        if url[last_index] != " ":
            url[i] = url[last_index]
        else:
            i -= 2
            url[i:i+3] = "{}".format("%20")

        i -= 1
        last_index -= 1

    # debug
    print("{}".format("".join(url)), len(url))

# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
