import sys


# -----------------------------------------------------------------------------|
def main():
	"""

	"""

	n = int(input())
	matrix = []

	for _ in range(n):
		matrix.append([int(x) for x in input().split()])

	# debug
	print("matrix = {}".format(matrix))

	bitset_col = [0 for _ in range(n)]
	bitset_row = [0 for _ in range(n)]

	for i in range(n):
		for j in range(n):
			if matrix[i][j] == 0:
				bitset_row[i] = 1
				bitset_col[j] = 1

	zero_col(matrix, bitset_col)
	zero_row(matrix, bitset_row)

# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def zero_col(matrix, bitset_col):
	"""

	"""

	for col_index in bitset_col:
		if col_index == 1:
			for row in matrix:
				row[col_index] = 0


# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def zero_row(matrix, bitset_row):
	"""

	"""

	for row_index in bitset_row:
		if row_index == 1:
			matrix[row_index] = [0 for _ in range(len(matrix))]

# -----------------------------------------------------------------------------|


if __name__ == '__main__':
	main()
