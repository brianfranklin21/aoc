"""https://adventofcode.com/2022/day/13"""

from __future__ import annotations
from ast import literal_eval


class DayThirteen:
    """Top-level class to solve the day's puzzles."""

    def __init__(self, input_fname: str) -> None:
        """Read and parse the input file."""
        with open(input_fname, 'r') as f:
            data_gen = (pair.splitlines() for pair in f.read().split('\n\n'))
            self.data = [tuple(map(literal_eval, pair)) for pair in data_gen]
            # print(self.data)

    def is_correct_order(self, L: int | list, R: int | list) -> int:
        """Return 1 if l & r are in the correct order, 0 if tie, -1 if not."""
        match L, R:
            case int(), int():
                return (L < R) - (R < L)

            case int(), list():
                return self.is_correct_order([L], R)

            case list(), int():
                return self.is_correct_order(L, [R])

            case list(), list():
                # Note: map stops when the shortest argument iterable is exhausted.
                for x in map(self.is_correct_order, L, R):
                    if x:
                        return x
                # Still a tie so final comparison is made by length.
                return self.is_correct_order(len(L), len(R))

            case _:
                raise ValueError

    def part1(self) -> None:
        """Solve the puzzle for part 1."""
        ans = sum(i for i, p in enumerate(self.data, start=1) if self.is_correct_order(*p) > 0)
        print(f"Part 1: {ans}")

    def part2(self) -> None:
        """Solve the puzzle for part 2."""
        print(f"Part 2: {0}")


# day13 = DayThirteen("sample.txt")
day13 = DayThirteen("input.txt")
day13.part1()
day13.part2()
