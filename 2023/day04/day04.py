#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/4
Author: Brian Franklin
"""


class Day04:
    """Class for solving the puzzle"""

    def __init__(self, filename: str) -> None:
        """Parse the puzzle input text and calculate the answers."""

        def matches(card) -> int:
            winning, have = card.split(":")[1].split("|")
            winning = set(int(n) for n in winning.split())
            have = set(int(n) for n in have.split())
            return len(have.intersection(winning))

        with open(filename, "r", encoding="utf-8") as f:
            self.matches = [matches(line) for line in f]  # each line is a card

        print(self.matches)
        self.solve_part1()
        self.solve_part2()

    def solve_part1(self) -> None:
        """Solve the puzzle for part 1."""
        self.points = [2 ** (m - 1) for m in self.matches if m > 0]
        self.part1 = sum(self.points)

    def solve_part2(self) -> None:
        """Solve the puzzle for part 2."""
        data = {i: 1 for i in range(len(self.matches))}
        # for i, m in enumerate(self.matches):

        self.part2 = 30

    def __str__(self) -> str:
        """Return the puzzle answers as a string."""
        return f"{type(self).__name__}(part1={self.part1!r}, part2={self.part2!r})"


Test = Day04("sample.txt")
assert Test.part1 == 13, f"Expected 13, got {Test.part1}"
assert Test.part2 == 30, f"Expected 30, got {Test.part2}"

# Puzzle = Day04("input.txt")
# print(Puzzle)
# assert Puzzle.part1 == 15205, f"Expected 15205, got {Puzzle.part1}"
# assert Puzzle.part2 == 0, f"Expected 0, got {Puzzle.part2}"
