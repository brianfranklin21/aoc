#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/3
Author: Brian Franklin
"""
import re, math
from collections import defaultdict


class Day03:
    """Class for solving the puzzle"""

    def __init__(self, filename: str) -> None:
        """Parse the puzzle input text and calculate the answers."""
        with open(filename, "r", encoding="utf-8") as f:
            # self.data = [line.split() for line in f]
            self.data = list(f)
        self.solve_part1()
        self.solve_part2()

    def solve_part1(self) -> None:
        """Solve the puzzle for part 1."""
        r_max = len(self.data)
        c_max = len(self.data[0]) - 1

        self.symbols = {
            (r, c): self.data[r][c]
            for r in range(r_max)
            for c in range(c_max)
            if self.data[r][c] not in "0123456789."
        }

        self.numbers = {
            (r, (n.start(), n.end())): int(n.group())
            for r, row in enumerate(self.data)
            for n in re.finditer(r"\d+", row)
        }

        self.part_numbers = defaultdict(list)
        for (r, (c1, c2)), v in self.numbers.items():
            edge = {(r, c) for r in (r - 1, r, r + 1) for c in range(c1 - 1, c2 + 1)}
            for rs, cs in edge & self.symbols.keys():
                self.part_numbers[rs, cs].append(v)

        # print(self.symbols)
        # print(self.numbers)
        # print(self.part_numbers)
        pn_flat_list = sum(self.part_numbers.values(), [])  # using sum as list concat
        self.part1 = sum(pn_flat_list)

    def solve_part2(self) -> None:
        """Solve the puzzle for part 2."""
        self.part2 = sum(
            math.prod(p) for p in self.part_numbers.values() if len(p) == 2
        )

    def __str__(self) -> str:
        """Return the puzzle answers as a string."""
        return f"{type(self).__name__}(part1={self.part1!r}, part2={self.part2!r})"


Test = Day03("sample.txt")
assert Test.part1 == 4361, f"Expected 4361, got {Test.part1}"
assert Test.part2 == 467835, f"Expected 467835, got {Test.part2}"

Puzzle = Day03("input.txt")
print(Puzzle)
assert Puzzle.part1 == 553079, f"Expected 553079, got {Puzzle.part1}"
assert Puzzle.part2 == 84363105, f"Expected 84363105, got {Puzzle.part2}"
