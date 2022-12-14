""" https://adventofcode.com/2022/day/12
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque


@dataclass(frozen=True)
class Point():
    """ Dataclass to hold point coordinates with a method to return neighbors.
    """
    x: int
    y: int

    def neighbors(self) -> list[Point]:
        """ Returns a list of points L, R, U, D from this point.
        """
        return [Point(self.x + dx, self.y + dy) for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))]


class Grid():
    """ Implements a 2D grid of Point objects and pathfinding methods.
    """
    def __init__(self, grid_array: list[str]) -> None:
        """ Generate Grid instance from 2D array.
        """
        self.array = grid_array
        self.x_size = len(self.array[0])
        self.y_size = len(self.array)
        self.start = self._get_point_where("S")
        self.end = self._get_point_where("E")

    def all_lowest_elevation_points(self) -> set[Point]:
        all_points = [Point(x, y) for x in range(self.x_size) for y in range(self.y_size)]
        low_points = {
            point for point in all_points
            if self.array[point.y][point.x] == "a" or self.array[point.y][point.x] == "S"
        }
        return low_points

    def _get_point_where(self, x: str) -> Point:
        """ Returns the point where "S" or "E" are located.
        """
        for row_num, row in enumerate(self.array):
            if x in row:
                return Point(row.index(x), row_num)

    def elev_at(self, point: Point) -> int:
        """ Returns the elevation at a point. Maps [a:z] to [96:122] using ord().
        """
        if point == self.start:
            return ord("a")

        if point == self.end:
            return ord("z")

        return ord(self.array[point.y][point.x])

    def _point_in_grid(self, point: Point) -> bool:
        """ Returns True if the point is within the grid.
        """
        return (0 <= point.x < self.x_size and 0 <= point.y < self.y_size)

    def _valid_neighbors(self, location: Point):
        """ Yields the valid neighbor points. Move is allowed if elevation is <= 1 + current elev.
        """
        current_elev = self.elev_at(location)

        for neighbor in location.neighbors():
            if self._point_in_grid(neighbor) and self.elev_at(neighbor) <= current_elev + 1:
                yield neighbor

    def get_path(self, start: Point):
        """ Given a start point, determine best path to reach the end specified by 'E'.
            Returns a list of points that make up the path, or None if no valid path.
        """
        points_to_check: deque[Point] = deque()
        points_to_check.append(start)

        came_from = {}
        came_from[start] = None

        while points_to_check:
            point = points_to_check.popleft()

            if point == self.end:
                break

            for neighbor in self._valid_neighbors(point):
                if neighbor not in came_from:
                    points_to_check.append(neighbor)
                    came_from[neighbor] = point

        if point != self.end:
            return None

        # build path by retracing the breadcrumbs
        point = self.end
        path = []
        while point != start:
            path.append(point)
            point = came_from[point]

        return path

    def __repr__(self) -> str:
        """ Prints the 2D grid
        """
        return "\n".join("".join(map(str, row)) for row in self.array)


class DayTwelve:
    """ Top-level class for solving part1 and part2 puzzles.
    """
    def __init__(self, input_fname):
        """ Reads and parses the input file and creates the 2D grid object.
        """
        with open(input_fname, 'r') as _file:
            self.data = _file.read().splitlines()

        self.grid = Grid(self.data)

    def part1(self):
        """ What is the fewest steps required to move from your current position
            to the location that should get the best signal?
        """
        path = self.grid.get_path(self.grid.start)
        self.p1_length = len(path)
        print(f"Part 1: {self.p1_length}")

    def part2(self):
        """ What is the fewest steps required to move starting from any square
            with elevation a to the location that should get the best signal?
        """
        start_points = self.grid.all_lowest_elevation_points()
        self.p2_length = self.p1_length
        for start in start_points:
            path = self.grid.get_path(start)
            if path:
                self.p2_length = min(self.p2_length, len(path))
        print(f"Part 2: {self.p2_length}")


# day12 = DayTwelve("sample.txt")
day12 = DayTwelve("input.txt")
day12.part1()
day12.part2()
