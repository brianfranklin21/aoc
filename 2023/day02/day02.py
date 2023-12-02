#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/2
Author: Brian Franklin
"""
from math import prod


class Day02:
    """Class for solving the puzzle"""

    def __init__(self, filename: str) -> None:
        """Parse the puzzle input text and calculate the answers."""
        self.data = {}
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                game_id, line = line.rstrip().split(": ")
                game_id = int(game_id.split()[-1])
                self.data[game_id] = line
        # print(self.data)
        self.solve_part1()
        self.solve_part2()

    def solve_part1(self) -> None:
        """Solve the puzzle for part 1."""
        g_max = {"red": 12, "green": 13, "blue": 14}
        valid_games = set()
        for game_id, line in self.data.items():
            valid_games.add(game_id)
            for reveal in line.split("; "):
                for cube in reveal.split(", "):
                    num, color = cube.split()
                    if int(num) > g_max[color]:
                        valid_games.discard(game_id)
        self.part1 = sum(valid_games)

    def solve_part2(self) -> None:
        """Solve the puzzle for part 2."""
        result = {}
        for game_id, line in self.data.items():
            g_min = {"red": 0, "green": 0, "blue": 0}
            for reveal in line.split("; "):
                for cube in reveal.split(", "):
                    num, color = cube.split()
                    g_min[color] = max(g_min[color], int(num))
            result[game_id] = prod(g_min.values())
        self.part2 = sum(result.values())

    def __str__(self) -> str:
        """Return the puzzle answers as a string."""
        return f"{type(self).__name__}(part1={self.part1!r}, part2={self.part2!r})"


Test = Day02("sample.txt")
print(Test)
assert Test.part1 == 8, f"Expected 8, got {Test.part1}"
assert Test.part2 == 2286, f"Expected 2286, got {Test.part2}"

Puzzle = Day02("input.txt")
print(Puzzle)
assert Puzzle.part1 == 2348, f"Expected 2348, got {Puzzle.part1}"
assert Puzzle.part2 == 76008, f"Expected 76008, got {Puzzle.part2}"
