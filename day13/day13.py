"""https://adventofcode.com/2022/day/13"""

from __future__ import annotations
from ast import literal_eval
from functools import cmp_to_key
from math import prod


class DayThirteen:
    """Top-level class to solve the day's puzzles."""

    def __init__(self, input_fname: str) -> None:
        """Read and parse the input file."""
        with open(input_fname, 'r') as f:
            data_gen = (pair.splitlines() for pair in f.read().split('\n\n'))
            self.data = [tuple(map(literal_eval, pair)) for pair in data_gen]
            # print(self.data)

    def compare(self, L: int | list, R: int | list) -> int:
        """Comparison Function. Return -1 for less-than, 0 for equal, or 1 for greater-than"""
        match L, R:
            case int(), int():
                return (L > R) - (L < R)

            case int(), list():
                return self.compare([L], R)

            case list(), int():
                return self.compare(L, [R])

            case list(), list():
                # Note: map stops when the shortest argument iterable is exhausted.
                for x in map(self.compare, L, R):
                    if x:
                        return x
                # Still a tie so final comparison is made by length.
                return self.compare(len(L), len(R))

            case _:
                raise ValueError

    def part1(self) -> None:
        """Solve the puzzle for part 1."""
        ans = sum(i for i, p in enumerate(self.data, start=1) if self.compare(*p) < 0)
        print(f"Part 1: {ans}")

    def part2(self) -> None:
        """Solve the puzzle for part 2."""
        packets = [[[2]], [[6]]]
        for L, R in self.data:
            packets.append(L)
            packets.append(R)

        packets = sorted(packets, key=cmp_to_key(self.compare))
        ans = prod(i for i, p in enumerate(packets, start=1) if p in ([[2]], [[6]]))
        print(f"Part 2: {ans}")


# day13 = DayThirteen("sample.txt")
day13 = DayThirteen("input.txt")
day13.part1()
day13.part2()
