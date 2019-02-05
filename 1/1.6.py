import sys


# -----------------------------------------------------------------------------|
def main():
	"""
	"""
	input_str = sys.argv[1]
	new_str = []

	current_count = 0
	current_ch = input_str[0]
	for i, ch in enumerate(input_str):
		if ch != current_ch:
			new_str.append(current_ch)
			new_str.append(str(current_count))
			current_count = 1
			current_ch = ch
		else:
			current_count += 1

	new_str.append(current_ch)
	new_str.append(str(current_count))
	# debug
	print("new_str = {}".format(min(("".join(new_str), input_str), key=len)))

# -----------------------------------------------------------------------------|


if __name__ == '__main__':
	main()
