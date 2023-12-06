def load_lines(path: str):
    with open(path, "r") as file:
        return file.readlines()


def find_number(line: str) -> int:
    for letter in line:
        if letter.isnumeric():
            return letter


def main():
    result = 0
    for word in load_lines("./input.txt"):
        number = find_number(word) + find_number(reversed(word))
        result += int(number)
    print(result)


if __name__ == "__main__":
    main()
