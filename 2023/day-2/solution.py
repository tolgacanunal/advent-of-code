import os
import re
from typing import Callable

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")

BLUE_KEYWORD = "blue"
RED_KEYWORD = "red"
GREEN_KEYWORD = "green"

RED_THRESHOLD = 12
GREEN_THRESHOLD = 13
BLUE_THRESHOLD = 14


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    prefix_removed = re.sub(r'Game \d+: ', '', file_content)
    return prefix_removed


def do_operation_for_each_line(
    prefix_removed,
    each_line_needed_func: Callable[[int, int, int], int]
) -> str:
    count = 0
    for id, game in enumerate(prefix_removed.split("\n")):
        max_red, max_green, max_blue = 0, 0, 0

        for each_round in game.split(";"):
            for each_pick in each_round.split(","):
                amount_of_cubes = int(each_pick.strip().split(" ")[0])
                if each_pick.endswith(BLUE_KEYWORD):
                    max_blue = max(max_blue, amount_of_cubes)
                elif each_pick.endswith(RED_KEYWORD):
                    max_red = max(max_red, amount_of_cubes)
                elif each_pick.endswith(GREEN_KEYWORD):
                    max_green = max(max_green, amount_of_cubes)

        count += each_line_needed_func(id + 1, max_red, max_green, max_blue)

    return count


def get_part_one_solution(prefix_removed: str) -> str:
    def operation(id, max_red, max_green, max_blue) -> int:
        if max_blue <= BLUE_THRESHOLD and max_green <= GREEN_THRESHOLD and max_red <= RED_THRESHOLD:
            return id
        else:
            return 0

    return do_operation_for_each_line(prefix_removed, operation)


def get_part_two_solution(s: str) -> str:
    def operation(_, red, green, blue) -> int:
        return blue * red * green

    return do_operation_for_each_line(s, operation)


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
