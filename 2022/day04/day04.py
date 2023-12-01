""" https://adventofcode.com/2022/day/4
"""
import time


class DayFour:

    def __init__(self, input_fname):
        self.data = []
        with open(input_fname, 'r') as _file:
            for line in _file:
                line = line.strip()
                self.data.append(
                    tuple([int(i) for r in line.split(',') for i in r.split('-')])
                )

    def full_overlap(self, lb1, ub1, lb2, ub2):
        set1_in_set2 = lb1 >= lb2 and ub1 <= ub2
        set2_in_set1 = lb2 >= lb1 and ub2 <= ub1
        return set1_in_set2 or set2_in_set1

    def any_overlap(self, lb1, ub1, lb2, ub2):
        return not ((ub1 < lb2) or (ub2 < lb1))

    def part1(self):
        return sum([self.full_overlap(*i) for i in self.data])

    def part2(self):
        return sum([self.any_overlap(*i) for i in self.data])

    def print_results(self):
        t0 = time.time()
        ans1 = self.part1()
        t1 = (time.time() - t0) * 1000000
        t0 = time.time()
        ans2 = self.part2()
        t2 = (time.time() - t0) * 1000000
        print(f"part1 ({t1:.3f} µs) = {ans1}\n"
              f"part2 ({t2:.3f} µs) = {ans2}")

    def full_overlap_alt(self, lb1, ub1, lb2, ub2):
        set1 = set(range(lb1, ub1 + 1))
        set2 = set(range(lb2, ub2 + 1))
        return set1.issuperset(set2) or set2.issuperset(set1)

    def any_overlap_alt(self, lb1, ub1, lb2, ub2):
        set1 = set(range(lb1, ub1 + 1))
        set2 = set(range(lb2, ub2 + 1))
        return set1 & set2 != set()

    def part1_alt(self):
        return sum([self.full_overlap_alt(*i) for i in self.data])

    def part2_alt(self):
        return sum([self.any_overlap_alt(*i) for i in self.data])

    def print_results_alt(self):
        t0 = time.time()
        ans1 = self.part1_alt()
        t1 = (time.time() - t0) * 1000000
        t0 = time.time()
        ans2 = self.part2_alt()
        t2 = (time.time() - t0) * 1000000
        print(f"part1_alt ({t1:.3f} µs) = {ans1}\n"
              f"part2_alt ({t2:.3f} µs) = {ans2}")


# day4 = DayFour("sample.txt")
day4 = DayFour("input.txt")
day4.print_results()
day4.print_results_alt()
