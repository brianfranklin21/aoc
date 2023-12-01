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
            dt = -1
            for row in self.df0.index[::-1]:
                if dt < self.df0.loc[row, col]:
                    dt = self.df0.loc[row, col]
                    self.df1.loc[row, col] = 1
        # display(self.df1)
        print(self.df1.sum().sum())

    def score(self, row, col):
        max_col = self.df0.columns[-1]
        max_row = self.df0.index[-1]
        # look left
        ls = 0
        if col > 0:
            v = self.df0.loc[row, 0:col].tolist()[::-1]
            for i in v[1:]:
                ls += 1
                if i >= v[0]:
                    break
        # look right
        rs = 0
        if col < max_col:
            v = self.df0.loc[row, col:].tolist()
            for i in v[1:]:
                rs += 1
                if i >= v[0]:
                    break
        # look up
        us = 0
        if row > 0:
            v = self.df0.loc[0:row, col].tolist()[::-1]
            for i in v[1:]:
                us += 1
                if i >= v[0]:
                    break
        # look down
        ds = 0
        if row < max_row:
            v = self.df0.loc[row:, col].tolist()
            for i in v[1:]:
                ds += 1
                if i >= v[0]:
                    break
        return ls * rs * us * ds

    def part2(self):
        """ What is the highest scenic score possible for any tree?
        """
        self.df2 = self.df0.copy()
        self.df2.loc[:, :] = 0
        for row in self.df0.index:
            for col in self.df0.columns:
                self.df2.loc[row, col] = self.score(row, col)
        print(self.df2)
        print(self.df2.max().max())


# day8 = DayEight("sample.txt")
day8 = DayEight("input.txt")
day8.part1()
day8.part2()
