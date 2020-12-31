from pathlib import Path
from typing import List, Tuple
import re
import string

from utils import open_puzzle_input


# DAG structure where each Node is a Bag Type, and A->B if 'B contains A'
# Solution is achieved by finding all reachable nodes from base node.
def day8_1() -> int:
    with open_puzzle_input(day=8) as fp:
        instructions = list(fp.readlines())


print("ex1 res: ", day8_1())
print("ex2 res: ", day8_2())

