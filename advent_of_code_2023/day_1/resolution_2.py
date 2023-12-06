from typing import Literal

def reverse_word(word):
    return word[-1::-1]


NUMBERS = (
    ('one', reverse_word('one'), '1'),
    ('two', reverse_word('two'), '2'),
    ('three', reverse_word('three'), '3'),
    ('four', reverse_word('four'), '4'),
    ('five', reverse_word('five'), '5'),
    ('six', reverse_word('six'), '6'),
    ('seven', reverse_word('seven'), '7'),
    ('eight', reverse_word('eight'), '8'),
    ('nine', reverse_word('nine'), '9'),
)

class NumberNotFound(Exception):
    ...


def load_lines(path: str):
    with open(path, "r") as file:
        return file.readlines()





def parse_numbers(word, reverse=False):
    num = ''
    while not num:
        try:
            num = get_number(word, reverse=reverse)
        except NumberNotFound:
            word = word[1:]    
    return num, word


def get_number(word, reverse=False) -> tuple[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9'], str]:
    pos = 1 if reverse is True else 0

    for number in NUMBERS:
        if word[0] == number[-1]:
            return number[-1]

        value = number[pos]
        if word[:len(value)] == value:
            return number[-1]
    raise NumberNotFound(f'check the string -> {word}')


if __name__ == '__main__':
    path = './input.txt'
    total = 0
    for word in load_lines(path):
        num1, word= (parse_numbers(word))
        num2, _ = (parse_numbers(reverse_word(word), reverse=True))
        total += int(num1 + num2)
        print(total)
