def print_mul_table():
	_9x9 = []

	for i in range(1, 10):
		row = []
		for j in range(1, 10):
			row.append("{}x{}={:2d}".format(i, j, i*j))
		_9x9.append(row)
	
	return _9x9


if __name__ == "__main__":
	for r in print_mul_table():
		print(r)

