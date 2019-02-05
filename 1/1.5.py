import sys


# -----------------------------------------------------------------------------|
def main():
	"""

	"""

	str1 = sys.argv[1]
	str2 = sys.argv[2]

	print(one_away(str1, str2))


# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def one_away(str1, str2):
	"""

	"""
	min_str = min((str1, str2), key = len)
	max_str = max((str1, str2), key = len)

	len_diff = len(max_str) - len(min_str)
	edit_done = False

	if len_diff > 1:
		return False
	elif len_diff == 0:
		# replace edit
		for i, ch in enumerate(str1):
			if ch != str2[i]:
				if edit_done:
					return False
				edit_done = True
	elif len_diff == 1:
		j = 0
		# delete edit
		for ch in max_str[:-1]:
			if ch != min_str[j]:
				if edit_done:
					return False
				edit_done = True
				j -= 1
			j += 1

	return True
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
	main()
