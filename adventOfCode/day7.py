from pathlib import Path
from typing import List, Tuple
import networkx as nx
import re
import string

INPUT_PATH = Path("inputs/day7.txt")
PATTERN = r'(?P<outer>[\w+ ]+) bags contain (?P<inner>(?:\d+ [\w+ ]+ bag[s]?[,.]?[ ]?)+)'


# input: "4 muted yellow bags,"
# output: ("muted yellow", 4)
def extract_inner_bag_attr(inner_str: str) -> Tuple[str, int]:
    num = [int(s) for s in inner_str.split() if s.isdigit()][0]
    item = inner_str.translate(str.maketrans('', '', string.digits))
    item = item.replace(".", "")
    if "bags" in item:
        item = item.replace("bags", "")
    else:
        item = item.replace("bag", "")
    item = item.lstrip().rstrip()
    return item, num


# input: "wavy purple bags contain 1 drab white bag, 4 muted yellow bags, 2 wavy aqua bags."
# output: ("wavy purple", [("drab white", 1), ("muted yellow", 4), ("wavy aqua", 2)])
def parse_outer_and_inner_from_text(line: str) -> Tuple[str, List[Tuple[str, int]]]:
    m = re.match(PATTERN, line)
    if m:
        inner_str = m.group("inner")
        inner = [extract_inner_bag_attr(item) for item in inner_str.split(",")]
        return m.group("outer"), inner


# DAG structure where each Node is a Bag Type, and A->B if 'B contains A'
# Solution is achieved by finding all reachable nodes from base node.
def day7_1() -> int:
    DG = nx.DiGraph()
    with open(INPUT_PATH) as fp:
        for line in fp:
            if "contain no" in line:
                continue
            outer, inner_list = parse_outer_and_inner_from_text(line.strip('\n'))
            DG.add_edges_from([(inner, outer)
                               for inner, _ in inner_list])

    return len(nx.descendants(DG, "shiny gold"))


# Recursive Solution using a DAG.
# Edges direction is the opposite from day7_1, and weights are added accordingly to represent
# the number of bags needed
def day7_2() -> int:
    DG = nx.DiGraph()
    with open(INPUT_PATH) as fp:
        for line in fp:
            if "contain no" in line:
                continue
            outer, inner_list = parse_outer_and_inner_from_text(line.strip('\n'))
            for inner, weight in inner_list:
                DG.add_edge(outer, inner, weight=weight)

    return find_num_bags_inside(DG, "shiny gold")


# recursive function to calculate the bags needed
def find_num_bags_inside(dg: nx.DiGraph, base_node) -> int:
    bags = 0
    neighbors = nx.neighbors(dg, base_node)
    if not neighbors:
        return 0
    for node in neighbors:
        weight = dg.edges[base_node, node]['weight']
        bags += weight * (1 + find_num_bags_inside(dg, node))
    return bags


if __name__ == "__main__":
    print("ex1 res: ", day7_1())
    print("ex2 res: ", day7_2())
