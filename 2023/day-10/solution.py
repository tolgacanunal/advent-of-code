from dataclasses import dataclass
import os
import sys

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


@dataclass(frozen=True)
class Point:
    x: int
    y: int


# pipe_char: moves you can make
def create_moves_hashmap() -> dict[str, list[Point]]:
    return {
        '|': [Point(0, -1), Point(0, 1)],
        '-': [Point(1, 0), Point(-1, 0)],
        'L': [Point(0, -1), Point(1, 0)],
        'J': [Point(0, -1), Point(-1, 0)],
        '7': [Point(-1, 0), Point(0, 1)],
        'F': [Point(0, 1), Point(1, 0)],
        'S': [Point(0, 1), Point(1, 0), Point(-1, 0), Point(0, -1)],
    }


def get_starting_point(lines: list[str]) -> Point:
    for vertical_index, line in enumerate(lines):
        for horizontal_index, char in enumerate(line):
            if char == 'S':
                return Point(horizontal_index, vertical_index)
    raise Exception("starting point cannot be found.")


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    map = [line for line in file_content.split("\n")]
    return map


def get_part_one_solution(map: list[str]) -> str:
    starting_point = get_starting_point(map)
    moves = create_moves_hashmap()

    current_point = starting_point
    last_point: Point = None

    step = 0
    while not last_point or current_point != starting_point:
        for move in moves[map[current_point.y][current_point.x]]:
            new_point = Point(current_point.x + move.x, current_point.y + move.y)
            if new_point != last_point:
                last_point = current_point
                current_point = new_point
                step += 1
                break  # only way to go through the pipes

    return step // 2


def get_part_two_solution(s: str) -> str:
    return "not solved yet."


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()

# 6717
