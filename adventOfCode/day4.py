from pathlib import Path

INPUT_PATH = Path("inputs/day4.txt")


def day4() -> int:
    items_seen = set()
    num_valid_passports = 0
    with open(INPUT_PATH) as fp:
        for idx, line in enumerate(fp):
            line = line.strip('\n')
            if line == "":
                if len(items_seen) == 8 or \
                        (len(items_seen) == 7 and "cid" not in items_seen):
                    num_valid_passports += 1
                items_seen.clear()
            else:
                if ' ' in line:
                    items = line.split(' ')
                    for item in items:
                        item_to_add = item.split(":")[0]
                        items_seen.add(item_to_add)
                else:
                    item_to_add = line.split(":")[0]
                    items_seen.add(item_to_add)

    return num_valid_passports


if __name__ == "__main__":
    print("ex1 res: ", day4())
