""" https://adventofcode.com/2022/day/10
"""


class Processor:

    def __init__(self) -> None:
        self.reg_x = [1, ]
        self.sprite = [0, 1, 2, ]
        self.crt = []

    def run(self, command) -> int:
        if command[0] == "noop":
            self.crt.append("#" if len(self.reg_x) in self.sprite else " ")
            self.reg_x.append(self.reg_x[-1])
        if command[0] == "addx":
            self.crt.append("#" if len(self.reg_x) in self.sprite else " ")
            self.reg_x.append(self.reg_x[-1])
            # second cycle:
            self.crt.append("#" if len(self.reg_x) in self.sprite else " ")
            self.reg_x.append(self.reg_x[-1] + int(command[1]))
            sprite_mid = self.reg_x[-1] + 1 + 40 * (len(self.reg_x) // 40)
            self.sprite = [sprite_mid - 1, sprite_mid, sprite_mid + 1]


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
        """ Render the image given by your program. What eight capital letters appear on your CRT?
        """
        cpu = Processor()
        for command in self.data:
            cpu.run(command)
        for i in range(0, 201, 40):
            print("".join(cpu.crt[i:40 + i]))


# day10 = DayTen("sample.txt")
day10 = DayTen("input.txt")
day10.part1()
day10.part2()
