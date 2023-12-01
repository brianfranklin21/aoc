"""https://adventofcode.com/2022/day/XX"""
from __future__ import annotations

# import itertools
# from dataclasses import dataclass


class DayXX:
    """Class for solving the day's puzzles.

    :ivar int part1: The answer to Part One.
    :ivar int part2: The answer to Part Two.
    :ivar ... data: The puzzle input parsed into ... .
    """

    def __init__(self, filename: str) -> None:
        """Parse the puzzle input and calculate the answers.

        :param str filename: File name of the puzzle input.
        """
        with open(filename, "r", encoding="utf-8") as f:
            self.data = [line.split() for line in f]

        self.solve_part1()
        self.solve_part2()

    def __str__(self) -> str:
        """Return the puzzle answers.

        :return str: The puzzle answers.
        """
        return f"{type(self).__name__}(part1={self.part1!r}, part2={self.part2!r})"

    def solve_part1(self) -> None:
        """Solve the puzzle for part 1."""
        self.part1 = 0

    def solve_part2(self) -> None:
        """Solve the puzzle for part 2."""
        self.part2 = 0


test = DayXX("sample.txt")
assert test.part1 == 0, f"Expected 0, got {test.part1}"
assert test.part2 == 0, f"Expected 0, got {test.part2}"

print(DayXX("input.txt"))
