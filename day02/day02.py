""" https://adventofcode.com/2022/day/2
"""


class DayTwo:

    def __init__(self, input_fname):
        self.guide = []
        with open(input_fname, 'r') as _file:
            for line in _file:
                self.guide.append(tuple(line.split()))

    def outcome(self, op, me):
        outcomes = {
            'A X': 'draw',
            'A Y': 'win',
            'A Z': 'loss',
            'B X': 'loss',
            'B Y': 'draw',
            'B Z': 'win',
            'C X': 'win',
            'C Y': 'loss',
            'C Z': 'draw',
        }
        return outcomes[f"{op} {me}"]

    def part1(self):
        """ What would your total score be if everything goes
            exactly according to your strategy guide?
        """
        shape_pts = {'X': 1, 'Y': 2, 'Z': 3}
        outcome_pts = {'loss': 0, 'draw': 3, 'win': 6}
        score = 0
        for op, me in self.guide:
            score += shape_pts[me] + outcome_pts[self.outcome(op, me)]
        print(f"score is {score}")


# day2 = DayTwo("sample_input.txt")
day2 = DayTwo("input.txt")
# print(day2.guide)
day2.part1()
