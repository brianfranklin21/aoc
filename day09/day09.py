""" https://adventofcode.com/2022/day/9
"""
import parse


class Rope:

    def __init__(self) -> None:
        self.head = (0, 0)  # row, col
        self.tail = (0, 0)  # row, col
        self.tail_log = {(0, 0), }

    def move_head(self, d, s) -> None:
        """     -
                U
            - L * R +
                D
                +
        """
        move = {
            'R': lambda x: (x[0], x[1] + 1),
            'L': lambda x: (x[0], x[1] - 1),
            'D': lambda x: (x[0] + 1, x[1]),
            'U': lambda x: (x[0] - 1, x[1]),
        }
        for _ in range(s):
            self.head = move[d](self.head)
            self._move_tail()

    def _move_tail(self) -> None:
        """   H H H
            H ↖️ ↑ ↗ H
            H ← T → H
            H ↙️ ↓ ↘ H
              H H H
        """
        move = {
            # head is R, L, D, or U
            (0,   2): lambda x: (x[0], x[1] + 1),
            (0,  -2): lambda x: (x[0], x[1] - 1),
            (2,   0): lambda x: (x[0] + 1, x[1]),
            (-2,  0): lambda x: (x[0] - 1, x[1]),
            # head is diagonal D R
            (1,   2): lambda x: (x[0] + 1, x[1] + 1),
            (2,   1): lambda x: (x[0] + 1, x[1] + 1),
            # head is diagonal D L
            (1,  -2): lambda x: (x[0] + 1, x[1] - 1),
            (2,  -1): lambda x: (x[0] + 1, x[1] - 1),
            # head is diagonal U R
            (-1,  2): lambda x: (x[0] - 1, x[1] + 1),
            (-2,  1): lambda x: (x[0] - 1, x[1] + 1),
            # head is diagonal U L
            (-1, -2): lambda x: (x[0] - 1, x[1] - 1),
            (-2, -1): lambda x: (x[0] - 1, x[1] - 1),
        }
        delta = tuple([self.head[0] - self.tail[0], self.head[1] - self.tail[1]])
        if 2 in delta or -2 in delta:
            self.tail = move[delta](self.tail)
            self.tail_log.add(self.tail)


class DayNine:

    def __init__(self, input_fname) -> None:
        with open(input_fname, 'r') as _file:
            self.data = [parse.search("{} {:d}", line).fixed for line in _file]

    def part1(self):
        """ How many positions does the tail of the rope visit at least once?
        """
        r = Rope()
        for direction, steps in self.data:
            r.move_head(direction, steps)
        print(len(r.tail_log))

    def part2(self):
        """
        """
        print()


# day9 = DayNine("sample.txt")
day9 = DayNine("input.txt")
day9.part1()
day9.part2()
