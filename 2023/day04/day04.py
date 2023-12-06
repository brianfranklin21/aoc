#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/4
Author: Brian Franklin
"""


class Day04:
    """Class for solving the puzzle"""

    def __init__(self, filename: str) -> None:
        """Parse the puzzle input text and calculate the answers."""
        with open(filename, "r", encoding="utf-8") as f:
            # self.data = [line.split() for line in f]
            self.data = list(f)
        # print(self.data)
        self.solve_part1()
        self.solve_part2()

    def solve_part1(self) -> None:
        """Solve the puzzle for part 1."""
        res = [0]
        # print(res)
        self.part1 = sum(res)

    def solve_part2(self) -> None:
        """Solve the puzzle for part 2."""
        res2 = [0]
        # print(res2)
        self.part2 = sum(res2)

    def __str__(self) -> str:
        """Return the puzzle answers as a string."""
        return f"{type(self).__name__}(part1={self.part1!r}, part2={self.part2!r})"


Test = Day04("sample.txt")
assert Test.part1 == 0, f"Expected 0, got {Test.part1}"
# assert Test.part2 == 0, f"Expected 0, got {Test.part2}"

# Puzzle = Day04("input.txt")
# print(Puzzle)
# assert Puzzle.part1 == 0, f"Expected 0, got {Puzzle.part1}"
# assert Puzzle.part2 == 0, f"Expected 0, got {Puzzle.part2}"
