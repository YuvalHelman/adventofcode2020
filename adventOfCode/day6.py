from pathlib import Path

INPUT_PATH = Path("inputs/day6.txt")


def day6_2() -> int:  # Everyone in group
    sum = 0
    first_item_flag = True
    with open(INPUT_PATH) as fp:
        intersection_set = set()
        for line in fp:
            line = line.strip('\n')
            if line == "":  # new group
                sum += len(intersection_set)
                intersection_set.clear()
                first_item_flag = True
            else:
                if first_item_flag:
                    intersection_set.update(list(line))
                    first_item_flag = False
                elif len(intersection_set) == 0:
                    continue
                else:
                    intersection_set = intersection_set.intersection(set(line))

    # EOF:
    sum += len(intersection_set)
    return sum


def day6_1() -> int:  # Anyone in group
    sum = 0
    with open(INPUT_PATH) as fp:
        counter = set()
        for idx, line in enumerate(fp):
            line = line.strip('\n')
            if line == "":  # new group
                sum += len(counter)
                counter.clear()
            else:
                counter.update(list(line))

    # EOF:
    sum += len(counter)
    return sum


if __name__ == "__main__":
    print("ex1 res: ", day6_1())
    print("ex2 res: ", day6_2())
