""" https://adventofcode.com/2022/day/6
"""


class DaySix:

    def __init__(self, input_fname):
        self.data = []
        with open(input_fname, 'r') as _file:
            for line in _file:
                line = line.strip()
                self.data.append(line)

    def find_marker(self, s, w):
        i = w
        while len(set(s[i-w:i])) < w:
            i += 1
        return i

    def part1(self):
        """ How many characters need to be processed before the first
            start-of-packet marker is detected?
        """
        for stream in self.data:
            print(self.find_marker(stream, 4))

    def part2(self):
        """ 14 distinct characters. How many characters need to be processed
            before the first start-of-packet marker is detected?
        """
        for stream in self.data:
            print(self.find_marker(stream, 14))


# day6 = DaySix("sample.txt")
day6 = DaySix("input.txt")
day6.part1()
day6.part2()
