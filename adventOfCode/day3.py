from pathlib import Path

INPUT_PATH = Path("inputs/day3.txt")


def day3(steps_right: int, steps_down: int = 1) -> int:
    num_of_cols = 31
    counter, col = 0, 0
    with open(INPUT_PATH) as fp:
        for idx, line in enumerate(fp):
            if idx == 0 or \
                    idx % steps_down != 0:
                continue
            col = (col + steps_right) % num_of_cols
            line = list(line.strip("\n"))
            if line[col] == '#':
                counter += 1
    return counter


if __name__ == "__main__":
    print("ex1 res: ", day3(3))

    mult = 1
    for steps_right, steps_down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        mult *= day3(steps_right, steps_down)
    print("ex2 res: ", mult)
