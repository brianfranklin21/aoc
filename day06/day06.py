""" https://adventofcode.com/2022/day/6
"""


class DaySix:

    def __init__(self, input_fname):
        self.data = []
        with open(input_fname, 'r') as _file:
            for line in _file:
                line = line.strip()
                self.data.append(line)

    def find_marker(self, s):
        i = 4
        while len(set(s[i-4:i])) < 4:
            # print(i, s[i-4:i], "fail")
            i += 1
        # print(i, s[i-4:i], "pass")
        return i

    def part1(self):
        """ How many characters need to be processed before the first
            start-of-packet marker is detected?
        """
        for stream in self.data:
            print(self.find_marker(stream))

    def part2(self):
        """
        """
        print()


# day6 = DaySix("sample.txt")
day6 = DaySix("input.txt")
day6.part1()
day6.part2()
