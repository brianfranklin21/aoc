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

    def my_shape(self, op_shape, outcome_code):
        my_shapes = {
            'A X': 'S',
            'A Y': 'R',
            'A Z': 'P',
            'B X': 'R',
            'B Y': 'P',
            'B Z': 'S',
            'C X': 'P',
            'C Y': 'S',
            'C Z': 'R',
        }
        return my_shapes[f"{op_shape} {outcome_code}"]

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

    def part2(self):
        """ Following the Elf's instructions for the second column, what would your
            total score be if everything goes exactly according to your strategy guide?
        """
        oc_map = {'X': 'loss', 'Y': 'draw', 'Z': 'win'}
        shape_pts = {'R': 1, 'P': 2, 'S': 3}
        outcome_pts = {'loss': 0, 'draw': 3, 'win': 6}
        score = 0
        for op, oc in self.guide:
            score += shape_pts[self.my_shape(op, oc)] + outcome_pts[oc_map[oc]]
        print(f"score is {score}")


# day2 = DayTwo("sample_input.txt")
day2 = DayTwo("input.txt")
day2.part1()
day2.part2()
