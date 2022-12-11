""" https://adventofcode.com/2022/day/10
"""


class Processor:

    def __init__(self) -> None:
        self.reg_x = [1, ]

    def run(self, command) -> int:
        prev = 1 if self.reg_x == [] else self.reg_x[-1]
        if command[0] == "noop":
            self.reg_x.append(prev)
        if command[0] == "addx":
            self.reg_x.append(prev)
            self.reg_x.append(prev + int(command[1]))


class DayTen:

    def __init__(self, input_fname):
        with open(input_fname, 'r') as _file:
            self.data = [line.strip().split() for line in _file]

    def signal_strength(self, reg_x, cycle):
        return reg_x[cycle] * cycle

    def part1(self):
        """ Find the signal strength during the 20th, 60th, 100th, 140th, 180th,
            and 220th cycles. What is the sum of these six signal strengths?
        """
        cpu = Processor()
        for command in self.data:
            cpu.run(command)
        signal_strength = sum([cpu.reg_x[i-1] * i for i in range(20, 221, 40)])
        print(signal_strength)

    def part2(self):
        """
        """
        print()


# day10 = DayTen("sample.txt")
day10 = DayTen("input.txt")
day10.part1()
day10.part2()
