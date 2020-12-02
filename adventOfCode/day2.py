from pathlib import Path
from typing import Callable
from itertools import filterfalse
import re

FILE_PATTERN = re.compile(r"(?P<min>[0-9]+)-(?P<max>[0-9]+)\s*(?P<letter_rule>[A-Za-z]):\s*(?P<password>[A-Za-z]+)")
INPUT_PATH = Path("inputs/day2_1.txt")


def is_count_of_char_in_sentence(char: str, sentence: str, min: int, max: int) -> bool:
    counter = len(list(filterfalse(lambda x: x is not char, sentence)))
    return min <= counter <= max


def day2(checker: Callable[..., bool]) -> int:
    counter = 0
    with open(INPUT_PATH) as fp:
        for line in fp:
            line = line.strip("\n")
            m = re.search(FILE_PATTERN, line)
            if m:
                if checker(m.group("letter_rule"), m.group("password"),
                                                int(m.group("min")), int(m.group("max"))):
                    counter += 1
                    print(line)
                    print(len(m.group("password")))
    return counter


def are_positions_valid(char: str, sentence: str, min: int, max: int) -> bool:
    counter = 0
    if len(sentence) >= min and sentence[min-1] == char:
        counter += 1
    if len(sentence) >= max and sentence[max - 1] == char:
        counter += 1
    return counter == 1

#
# def ex2():
#     counter = 0
#     with open(INPUT_PATH) as fp:
#         for line in fp:
#             m = re.search(FILE_PATTERN, line)
#             if m:
#                 if are_positions_valid(m.group("letter_rule"), m.group("password"),
#                                                 int(m.group("min")), int(m.group("max"))):
#                     counter += 1
#     return counter


if __name__ == "__main__":
    # print("ex1 res: ", day2(is_count_of_char_in_sentence))
    print("ex2 res: ", day2(are_positions_valid))
