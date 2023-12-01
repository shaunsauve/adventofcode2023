def decipher_document(document: str) -> int:
	sum = 0
	for line in document.split("\n"):
		if line.strip() == "":
			continue
		sum += decipher_line(line)
	return sum


def decipher_line(line: str) -> int:
	first_digit: [str, None] = None
	last_digit: [str, None] = None

	for i in range(len(line)):
		if line[i].isdigit():
			first_digit = line[i]
			break
	if not first_digit:
		raise ValueError("No digits found in line")

	for i in range(len(line) - 1, -1, -1):
		if line[i].isdigit():
			last_digit = line[i]
			break
	if not last_digit:
		raise ValueError(f"Last digit missing in '{line}'")

	return int(first_digit + last_digit)


example = """
		1abc2
		pqr3stu8vwx
		a1b2c3d4e5f
		treb7uchet
	"""

assert decipher_document(example) == 142

with open("day1.input", "r") as file:
	print(decipher_document(file.read()))


