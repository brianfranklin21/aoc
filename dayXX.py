#!/usr/bin/env python3
"""
https://adventofcode.com/2023/day/XX
Author: Brian Franklin
"""
import re


class DayXX:
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
        cal_data1 = []
        for line in self.data:
            if match := re.findall(r"\d", line):
                first_digit = match[0]
                last_digit = match[-1]
                cal_value = int("".join([first_digit, last_digit]))
                cal_data1.append(cal_value)
        # print(cal_data1)
        self.part1 = sum(cal_data1)

    def solve_part2(self) -> None:
        """Solve the puzzle for part 2."""
        cal_data2 = []
        for line in self.data:
            line = line.replace("one", "one1one")
            line = line.replace("two", "two2two")
            line = line.replace("three", "three3three")
            line = line.replace("four", "four4four")
            line = line.replace("five", "five5five")
            line = line.replace("six", "six6six")
            line = line.replace("seven", "seven7seven")
            line = line.replace("eight", "eight8eight")
            line = line.replace("nine", "nine9nine")
            if match := re.findall(r"\d", line):
                first_digit = match[0]
                last_digit = match[-1]
                cal_value = int("".join([first_digit, last_digit]))
                cal_data2.append(cal_value)
        # print(cal_data2)
        self.part2 = sum(cal_data2)

    def __str__(self) -> str:
        """Return the puzzle answers as a string."""
        return f"{type(self).__name__}(part1={self.part1!r}, part2={self.part2!r})"


Test = DayXX("sample.txt")
assert Test.part1 == 0, f"Expected 0, got {Test.part1}"
assert Test.part2 == 0, f"Expected 0, got {Test.part2}"

Puzzle = DayXX("input.txt")
print(Puzzle)
# assert Puzzle.part1 == 0, f"Expected 0, got {Puzzle.part1}"
# assert Puzzle.part2 == 0, f"Expected 0, got {Puzzle.part2}"
