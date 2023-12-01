""" https://adventofcode.com/2022/day/3
"""


class DayThree:

    def __init__(self, input_fname):
        self.data = []
        self.grp = []
        with open(input_fname, 'r') as _file:
            for line in _file:
                line = line.strip()
                mid = len(line) // 2
                self.data.append((line[:mid], line[mid:]))
                self.grp.append(line)
        self.grp = list(zip(self.grp[0::3], self.grp[1::3], self.grp[2::3]))

    def priority(self, item_type):
        """ ord('a') =  97 (0x61) --> priority = 1
            ord('z') = 122 (0x7A) --> priority = 26
            ord('A') =  65 (0x41) --> priority = 27
            ord('Z') =  90 (0x5A) --> priority = 52
        """
        priority = ord(item_type) - 38  # handles uppercase
        if priority > 52:
            priority -= 58  # handles lowercase
        return priority

    def part1(self):
        """ Find the item type that appears in both compartments of each rucksack.
            What is the sum of the priorities of those item types?
        """
        common_items = [(set(cmp1) & set(cmp2)).pop() for cmp1, cmp2 in self.data]
        priority_sum = sum([self.priority(i) for i in common_items])
        print(priority_sum)

    def part2(self):
        """ Find the item type that corresponds to the badges of each three-Elf group.
            What is the sum of the priorities of those item types?
        """
        badges = [(set(bag1) & set(bag2) & set(bag3)).pop() for bag1, bag2, bag3 in self.grp]
        priority_sum = sum([self.priority(i) for i in badges])
        print(priority_sum)


# day3 = DayThree("sample_input.txt")
day3 = DayThree("input.txt")
day3.part1()
day3.part2()
