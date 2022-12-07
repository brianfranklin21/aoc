""" https://adventofcode.com/2022/day/5
"""
import pandas as pd
import parse


class DayFive:

    def __init__(self, input_fname):
        self.stacks = []
        self.procedure = []
        pattern = parse.compile("move {:d} from {:d} to {:d}")
        with open(input_fname, 'r') as _file:
            section1 = True
            for line in _file:
                if line == '\n':
                    section1 = False
                    continue
                if section1:
                    self.stacks.append(list(line[1::4]))
                else:
                    self.procedure.append(pattern.search(line).fixed)
        self.data = {int(row[-1]): "".join(row[0:-1]).strip() for row in zip(*self.stacks)}

    def print_stacks(self):
        print(pd.DataFrame([list(i) for i in self.data.values()],
                           index=self.data.keys()).T.fillna(""), "\n")

    @property
    def top(self):
        return "".join([i[0] for i in self.data.values()])

    def run(self):
        self.print_stacks()
        for box_qty, from_stack, to_stack in self.procedure:
            for _ in range(box_qty):
                self.data[to_stack] = self.data[from_stack][0] + self.data[to_stack]
                self.data[from_stack] = self.data[from_stack][1:]
                self.print_stacks()

    def part1(self):
        """ After the rearrangement procedure completes, what crate ends up on top of each stack?
        """
        self.run()
        print(self.top)

    def part2(self):
        """
        """
        print()


# day5 = DayFive("sample.txt")
day5 = DayFive("input.txt")
day5.part1()
day5.part2()
