"""https://adventofcode.com/2022/day/14"""
from __future__ import annotations

import itertools
from dataclasses import dataclass

AIR = "."
ROCK = "#"
SAND = "o"


@dataclass(frozen=True)
class Point:
    """Class to represent an x,y coordinate.

    :param int x: Distance to the right.
    :param int y: Distance down.
    """

    x: int
    y: int


@dataclass(frozen=True)
class Block(Point):
    """Class to represent a cave block.

    :param int x: Distance to the right.
    :param int y: Distance down.
    :param str m: Material or type of block.
    """

    m: str


class Cave:
    """Class to represent a 2D cave with methods to manipulate the blocks in it.

    :ivar set[Block] blocks: A set of all the blocks in the cave.
    """

    def __init__(self) -> None:
        """Initialize the cave's set of blocks."""
        self.blocks: set[Block] = set()

    def add_rock(self, x: int, y: int) -> None:
        """Add a rock block to the cave at coordinates (x,y).

        :param int x: Distance to the right.
        :param int y: Distance down.
        """
        self.blocks.add(Block(x, y, ROCK))

    def add_rock_line(self, p0: Point, p1: Point) -> None:
        """Add a horizontal or vertical line of rock blocks to the cave.

        :param Point p0: Starting point of line of blocks.
        :param Point p1: Ending point of line of blocks.
        :raises ValueError: if dx and dy are both non-zero.
        """
        dx = p1.x - p0.x
        dy = p1.y - p0.y
        match dx, dy:
            # same start and stop point
            case 0, 0:
                self.add_rock(p0.x, p0.y)
            # vertical line
            case 0, _:
                y0, y1 = (p0.y, p1.y) if dy > 0 else (p1.y, p0.y)
                for y in range(y0, y1 + 1):
                    self.add_rock(p0.x, y)
            # horizontal line
            case _, 0:
                x0, x1 = (p0.x, p1.x) if dx > 0 else (p1.x, p0.x)
                for x in range(x0, x1 + 1):
                    self.add_rock(x, p0.y)
            # error, not orthogonal
            case _, _:
                raise ValueError(f"Unexpected values for dx, dy: {dx}, {dy}")

    def count_fallen_sand(self) -> int:
        """Count how many sand blocks eventually come to rest after falling.

        :return int: Number of sand blocks that came to rest after falling.
        """
        sand_start = Point(500, 0)
        bottom = max(block.y for block in self.blocks) + 1
        # For each new block of sand (counting up indefinitely)...
        for i in itertools.count(start=1):
            cur_pos = sand_start
            # Let the sand block fall until it can't anymore, then exit the while loop.
            while True:
                # If the sand block has fallen past the bottom then we're done.
                if cur_pos.y > bottom:
                    # This block didn't come to rest so total blocks at rest is previous count.
                    return i - 1
                # Try the three possible next moves in their order of priority.
                next_y = cur_pos.y + 1
                for next_x in (cur_pos.x, cur_pos.x - 1, cur_pos.x + 1):
                    if (
                        Block(next_x, next_y, ROCK) not in self.blocks
                        and Block(next_x, next_y, SAND) not in self.blocks
                    ):
                        # The sand block can move so move it and exit the for loop.
                        cur_pos = Point(next_x, next_y)
                        break
                # This for loop’s else clause only runs when exhausted, i.e. no breaks occurred.
                else:
                    # The sand block can't move so it has come to rest.
                    # Add it to the cave's set of blocks and exit the while loop.
                    self.blocks.add(Block(cur_pos.x, cur_pos.y, SAND))
                    break
        # We should never get here, but mypy complains without this return statement.
        return -1

    def plot(self) -> None:
        """Plot the cave blocks as a 2D text grid."""
        xs = [block.x for block in self.blocks]
        ys = [block.y for block in self.blocks]
        for y in range(min(ys), max(ys) + 1):
            print(f"{y} ", end="")
            for x in range(min(xs), max(xs) + 1):
                if Block(x, y, ROCK) in self.blocks:
                    print(ROCK, end="")
                elif Block(x, y, SAND) in self.blocks:
                    print(SAND, end="")
                else:
                    print(AIR, end="")
            print()


class Day14:
    """Class for solving the day's puzzles.

    :ivar int part1: The answer to Part One.
    :ivar int part2: The answer to Part Two.
    :ivar list[list[Point]] data: The puzzle input parsed into lists of rock path vertices.
    """

    def __init__(self, filename: str) -> None:
        """Parse the puzzle input and calculate the answers.

        :param str filename: File name of the puzzle input.
        """
        with open(filename, "r", encoding="utf-8") as f:
            self.data = [[Point(*map(int, p.split(","))) for p in line.split(" -> ")] for line in f]
        self.cave = Cave()
        for path in self.data:
            for i, point in enumerate(path):
                if i == 0:
                    continue
                self.cave.add_rock_line(path[i - 1], point)
        self.solve_part1()
        self.solve_part2()

    def __str__(self) -> str:
        """Return the puzzle answers.

        :return str: The puzzle answers.
        """
        return f"{type(self).__name__}(part1={self.part1!r}, part2={self.part2!r})"

    def solve_part1(self) -> None:
        """Solve the puzzle for part 1."""
        self.part1 = self.cave.count_fallen_sand()

    def solve_part2(self) -> None:
        """Solve the puzzle for part 2."""
        self.part2 = 0


test = Day14("sample.txt")
test.cave.plot()
assert test.part1 == 24, f"Expected 24, got {test.part1}"
assert test.part2 == 0, f"Expected 0, got {test.part2}"

print(Day14("input.txt"))
