""" https://adventofcode.com/2022/day/9
"""
import parse


class KnottedRope():

    def __init__(self, knots) -> None:
        self.knots = [(0, 0), ] * knots  # (row, col)
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
            self.knots[0] = move[d](self.knots[0])
            self._update_knots()

    def _update_knots(self) -> None:
        """ K H H H K
            H ↖️ ↑ ↗ H
            H ← K → H
            H ↙️ ↓ ↘ H
            K H H H K
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
            (2,   2): lambda x: (x[0] + 1, x[1] + 1),
            # head is diagonal D L
            (1,  -2): lambda x: (x[0] + 1, x[1] - 1),
            (2,  -1): lambda x: (x[0] + 1, x[1] - 1),
            (2,  -2): lambda x: (x[0] + 1, x[1] - 1),
            # head is diagonal U R
            (-1,  2): lambda x: (x[0] - 1, x[1] + 1),
            (-2,  1): lambda x: (x[0] - 1, x[1] + 1),
            (-2,  2): lambda x: (x[0] - 1, x[1] + 1),
            # head is diagonal U L
            (-1, -2): lambda x: (x[0] - 1, x[1] - 1),
            (-2, -1): lambda x: (x[0] - 1, x[1] - 1),
            (-2, -2): lambda x: (x[0] - 1, x[1] - 1),
        }
        for i, knot in enumerate(self.knots):
            if i == 0:
                continue
            delta = tuple([self.knots[i-1][0] - knot[0], self.knots[i-1][1] - knot[1]])
            if 2 in delta or -2 in delta:
                self.knots[i] = move[delta](knot)
        self.tail_log.add(self.knots[-1])


class DayNine:

    def __init__(self, input_fname) -> None:
        with open(input_fname, 'r') as _file:
            self.data = [parse.search("{} {:d}", line).fixed for line in _file]

    def part1(self):
        """ How many positions does the tail of the rope visit at least once?
        """
        r = KnottedRope(2)
        for direction, steps in self.data:
            r.move_head(direction, steps)
        print(len(r.tail_log))

    def part2(self):
        """ Simulate your complete series of motions on a larger rope with ten knots.
            How many positions does the tail of the rope visit at least once?
        """
        r = KnottedRope(10)
        for direction, steps in self.data:
            r.move_head(direction, steps)
        print(len(r.tail_log))


# day9 = DayNine("sample.txt")
# day9 = DayNine("sample2.txt")
day9 = DayNine("input.txt")
day9.part1()
day9.part2()
