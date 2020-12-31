from typing import IO
from pathlib import Path
import contextlib
import sys
import json

import requests
import rich


def _assert(pred: bool, mes: str = None):
    if not pred:
        rich.print("[bold red]" + mes + "[/bold red]")
        sys.exit()


def get_cur_package_path() -> Path:
    return Path(__file__).parent


@contextlib.contextmanager
def open_puzzle_input(day: int) -> Path:
    config_path = Path(get_cur_package_path()) / 'aoc_request.json'
    _assert(config_path.exists(), "loading input for puzzle failed. retry")
    with open(config_path) as f:
        config = json.load(f)

    url = f'https://adventofcode.com/2020/day/{str(day)}/input'
    puz_in_path = get_cur_package_path() / f"inputs/day{str(day)}.txt"
    if not puz_in_path.exists():
        r = requests.get(url, cookies={'session': config['session_id']},
                        headers={'User-Agent': config['user_agent']})
        puz_in_path.write_text(r.text)

    _assert(puz_in_path.exists(), "loading input for puzzle failed. retry")

    file_handle = open(puz_in_path)
    yield file_handle
    file_handle.close()

with open_puzzle_input(9) as f:
    print(list(f.readlines())[0])
