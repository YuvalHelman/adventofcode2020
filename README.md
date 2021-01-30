## [Advent Of Code 2020](https://adventofcode.com/2020)

Automatic Input download
---
- Use an automatic download of your input each time without copying it manually.

Add the file adventOfCode/aoc_requests.json with the format:

`{
    "session_id":"CopyFromBrowser",
    "user_agent":"CopyFromBrowser"
}`

and use inside the code:

```
from utils import open_puzzle_input

with open_puzzle_input(day=1, year=2020) as fp:
    print(fp.readlines())
```