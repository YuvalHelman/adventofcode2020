import re
from typing import Dict, List, Tuple

from utils import open_puzzle_input

PATTERN = r'(?P<instruction>\w+) (?P<sign>[+-])(?P<number>\d+)'
INDX_SET = set()


def parse_instruction(inst: str) -> Dict:
    m = re.match(PATTERN, inst)
    if m:
        return {
            "instruction": m["instruction"],
            "sign": m["sign"],
            "number": m["number"],
            "seen": False
        }


def recrs_walk_instructions(instructions: List, index: int, acc: int) -> Tuple[int, bool]:
    if index == len(instructions):
        return acc, True
    instruction = instructions[index]["instruction"]

    if instructions[index]["seen"]:
        return acc, False

    instructions[index]["seen"] = True
    INDX_SET.add(index)

    if instruction == "nop":
        return recrs_walk_instructions(instructions, index + 1, acc)

    if instructions[index]["sign"] == "+":
        signed_num = int(instructions[index]["number"])
    else:
        signed_num = -int(instructions[index]["number"])

    if instruction == "acc":
        return recrs_walk_instructions(instructions, index + 1, acc + signed_num)
    if instruction == "jmp":
        return recrs_walk_instructions(instructions, index + signed_num, acc)


def day8_1() -> int:
    with open_puzzle_input(day=8) as fp:
        instructions = [parse_instruction(inst) for inst in fp.readlines()]
        return recrs_walk_instructions(instructions, 0, 0)[0]


def day8_2() -> int:
    with open_puzzle_input(day=8) as fp:
        instructions = [parse_instruction(inst) for inst in fp.readlines()]
        recrs_walk_instructions(instructions, 0, 0)

    # Stuff to rule out:
    # 1. nop +0 is redundant to change.
    # 2. any index not seen before or inside the initial circle, is redundant to be changed.
    # 3. if a 'jmp' instruction's next index is 'seen' already, not reason to change it to 'nop'
    filtered_indx_set = {index for index in INDX_SET
                         if (instructions[index]["instruction"] == 'nop' and
                             not instructions[index]["number"] == "0")
                         or
                         (instructions[index]["instruction"] == 'jmp' and
                          not instructions[index + 1]["seen"])
                         }

    for index in filtered_indx_set:
        with open_puzzle_input(day=8) as fp:
            instructions = [parse_instruction(inst) for inst in fp.readlines()]
        instruction = instructions[index]["instruction"]
        if instruction == 'nop':
            instructions[index]["instruction"] = 'jmp'
        elif instruction == 'jmp':
            instructions[index]["instruction"] = 'nop'

        acc_res, is_done = recrs_walk_instructions(instructions, 0, 0)
        if is_done:
            return acc_res
        # change back
        instructions[index]["instruction"] = instruction


print("ex1 res: ", day8_1())
print("ex2 res: ", day8_2())
