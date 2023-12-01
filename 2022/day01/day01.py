""" https://adventofcode.com/2022/day/1
"""


class CaloriesList:

    def __init__(self, input_fname):
        self.data = {}
        with open(input_fname, 'r') as _file:
            elf = 1
            for line in _file:
                if line == '\n':
                    elf += 1
                    continue
                if elf not in self.data:
                    self.data[elf] = 0
                self.data[elf] += int(line)
        self.sorted_data = dict(sorted(self.data.items(), key=lambda i: i[1], reverse=True))

    def part1(self):
        """ Find the Elf carrying the most Calories.
            How many total Calories is that Elf carrying?
        """
        elves, cals = zip(*self.sorted_data.items())
        print(f"Elf {elves[0]} carries the most calories: {cals[0]}")

    def part2(self):
        """ Find the top three Elves carrying the most Calories.
            How many Calories are those Elves carrying in total?
        """
        elves, cals = zip(*self.sorted_data.items())
        print(f"Top three Elves {elves[:3]} carry the most calories totaling: {sum(cals[:3])}")


# cals = CaloriesList("sample_input.txt")
cals = CaloriesList("input.txt")
cals.part1()
cals.part2()
