from dataclasses import dataclass
import itertools
import os

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input.txt")


@dataclass
class Point:
    x: int
    y: int


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()

    lines = file_content.split("\n")

    points = [Point(i, j) for i, line in enumerate(lines) for j, cell in enumerate(line) if cell == '#']
    column_expansion = {v_index for v_index, line in enumerate(lines) if '#' not in line}
    row_expansion = {h_index for h_index, col in enumerate(zip(*lines)) if '#' not in col}

    return (points, row_expansion, column_expansion)


def get_distance_between(point_1: Point, point_2: Point) -> int:
    return abs(point_2.x - point_1.x) + abs(point_2.y - point_1.y)


def get_horizontal_expansion(point_1: Point, point_2: Point, column_expansion: set[int]) -> int:
    return len(column_expansion.intersection(range(min(point_1.x, point_2.x) + 1,  max(point_1.x, point_2.x))))


def get_vertical_expansion(point_1: Point, point_2: Point, row_expansion: set[int]) -> int:
    return len(row_expansion.intersection(range(min(point_1.y, point_2.y) + 1, max(point_1.y, point_2.y))))


def get_distance_betwen_every_point(data: tuple[list[Point], set[int], set[int]], expansion_multiplier: int) -> int:
    total = 0
    points, row_expansion, column_expansion = data
    for a, b in list(itertools.combinations(points, 2)):
        horizontal_expansion = get_horizontal_expansion(a, b, column_expansion) * expansion_multiplier
        vertical_expansion = get_vertical_expansion(a, b, row_expansion) * expansion_multiplier
        distance_without_expansion = get_distance_between(a, b)
        total += distance_without_expansion + horizontal_expansion + vertical_expansion
    return total


def get_part_one_solution(data: tuple[list[Point], set[int], set[int]]) -> str:
    return get_distance_betwen_every_point(data, 1)


def get_part_two_solution(data: tuple[list[Point], set[int], set[int]]) -> str:
    return get_distance_betwen_every_point(data, 999999)


def main():
    s: tuple[list[Point], set[int], set[int]] = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
