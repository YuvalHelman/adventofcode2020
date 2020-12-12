from pathlib import Path
import itertools

INPUT_PATH = Path("inputs/day5.txt")


def convert_ticket_to_id(ticket: str):
    replacement_rules = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    for k, v in replacement_rules.items():
        ticket = ticket.replace(k, v)

    row = int(ticket[:7], 2)
    column = int(ticket[7:], 2)
    return (row * 8) + column


def day5_1() -> int:
    best = 0
    with open(INPUT_PATH) as fp:
        for idx, line in enumerate(fp):
            line = line.strip('\n')
            id = convert_ticket_to_id(line)
            if id > best:
                best = id
    return best


def day5_2() -> int:
    best = 0
    items_set = set()
    for row, col in (itertools.product(range(0, 128), range(0, 8))):
        items_set.add((row * 8) + col)
    print(items_set)
    with open(INPUT_PATH) as fp:
        for line in fp:
            line = line.strip('\n')
            id = convert_ticket_to_id(line)
            items_set.remove(id)
    print(items_set)


if __name__ == "__main__":
    # convert_ticket_to_id("FFFBBBFRRR")
    # print("ex1 res: ", day5_1())
    print("ex2 res: ", day5_2())
