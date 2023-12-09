import os
import itertools
from collections import deque

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    return [list(map(int, line.split(" "))) for line in file_content.split("\n")]


def get_part_one_solution(histories: list[list[int]]) -> str:
    total = 0
    for start_history in histories:
        history_increment_levels: list[list[int]] = [start_history]
        while not all(map(lambda x: x == 0, history_increment_levels[-1])):
            paired_last_level = itertools.pairwise(history_increment_levels[-1])
            history_increment_levels.append([n2 - n1 for n1, n2 in paired_last_level])
        total += sum([level[-1] for level in history_increment_levels])
    return total


def get_part_two_solution(histories: list[list[str]]) -> str:
    total = 0
    for start_history in histories:
        history_increment_levels: list[list[int]] = [start_history]
        while not all(map(lambda x: x == 0, history_increment_levels[-1])):
            paired_last_level = itertools.pairwise(history_increment_levels[-1])
            history_increment_levels.append([n1 - n2 for n1, n2 in paired_last_level])
        total += sum([level[0] for level in history_increment_levels])
    return total


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
