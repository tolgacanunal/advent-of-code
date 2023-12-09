import os
import itertools
from collections import deque

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


def parse_input() -> list[list[int]]:
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    return [list(map(int, line.split(" "))) for line in file_content.split("\n")]


def get_part_one_solution(histories: list[list[int]]) -> str:
    return sum([sum([level[-1] for level in generate_increment_levels(history, False)]) for history in histories])


def get_part_two_solution(histories: list[list[str]]) -> str:
    return sum([sum([level[0] for level in generate_increment_levels(history, True)]) for history in histories])


def generate_increment_levels(base_level: list[int], reversed: bool) -> list[list[int]]:
    increment_levels: list[list[int]] = [base_level]
    while not all(map(lambda x: x == 0, increment_levels[-1])):
        paired_last_level = itertools.pairwise(increment_levels[-1])
        increment_levels.append([n1 - n2 if reversed else n2 - n1 for n1, n2 in paired_last_level])
    return increment_levels


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
