""" https://adventofcode.com/2022/day/8
"""
import pandas as pd


class DayEight:

    def __init__(self, input_fname):
        with open(input_fname, 'r') as f:
            data = f.readlines()
        self.df0 = pd.DataFrame([map(int, list(i.strip())) for i in data])
        print(self.df0)

    def part1(self):
        """ how many trees are visible from outside the grid?
        """
        self.df1 = self.df0.copy()
        self.df1.loc[:, :] = 0
        # look left and right
        for row in self.df0.index:
            lt = -1
            for col in self.df0.columns:
                if lt < self.df0.loc[row, col]:
                    lt = self.df0.loc[row, col]
                    self.df1.loc[row, col] = 1
            rt = -1
            for col in self.df0.columns[::-1]:
                if rt < self.df0.loc[row, col]:
                    rt = self.df0.loc[row, col]
                    self.df1.loc[row, col] = 1
        # look up and down
        for col in self.df0.columns:
            ut = -1
            for row in self.df0.index:
                if ut < self.df0.loc[row, col]:
                    ut = self.df0.loc[row, col]
                    self.df1.loc[row, col] = 1
            bt = -1
            for row in self.df0.index[::-1]:
                if bt < self.df0.loc[row, col]:
                    bt = self.df0.loc[row, col]
                    self.df1.loc[row, col] = 1
        print(self.df1)
        print(self.df1.sum().sum())

    def part2(self):
        """
        """
        print()


# day8 = DayEight("sample.txt")
day8 = DayEight("input.txt")
day8.part1()
day8.part2()
