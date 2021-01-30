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
def open_puzzle_input(day: int, year: int = 2020) -> Path:
    puz_in_path = get_cur_package_path() / f"inputs/day{str(day)}.txt"
    if not puz_in_path.exists():
        config_path = Path(get_cur_package_path()) / 'aoc_request.json'
        with open(config_path) as fp:
            config = json.load(fp)
        url = f'https://adventofcode.com/{year}/day/{str(day)}/input'
        r = requests.get(url, cookies={'session': config['session_id']},
                         headers={'User-Agent': config['user_agent']})
        puz_in_path.write_text(r.text)

    _assert(puz_in_path.exists(), "loading input for puzzle failed. retry")

    file_handle = puz_in_path.open()
    yield file_handle
    file_handle.close()


with open_puzzle_input(10) as f:
    print(list(f.readlines())[0])
