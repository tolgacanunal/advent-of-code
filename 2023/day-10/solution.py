from dataclasses import dataclass
from collections import deque
import os

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


# pipe_char: moves you can make
def create_moves_hashmap() -> dict[str, list[tuple[int, int]]]:
    return {
        '|': [(0, -1), (0, 1)],
        '-': [(1, 0), (-1, 0)],
        'L': [(0, -1), (1, 0)],
        'J': [(0, -1), (-1, 0)],
        '7': [(-1, 0), (0, 1)],
        'F': [(0, 1), (1, 0)],
        'S': [(0, 1), (0, -1), (1, 0), (-1, 0)],
    }


def get_starting_point(lines: list[str]) -> tuple[int, int]:
    for vertical_index, line in enumerate(lines):
        for horizontal_index, char in enumerate(line):
            if char == 'S':
                return (horizontal_index, vertical_index)
    raise Exception("starting point cannot be found.")


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    graph = [line for line in file_content.split("\n")]
    return graph

# if there's no loop, it will loop infinitely so loop or loop. :)


def get_loop_from_point(graph: list[str], starting_point: tuple[int, int]) -> set[tuple[int, int]]:
    moves = create_moves_hashmap()

    loop = set()
    current_point = starting_point

    while len(loop) == 0 or current_point != starting_point:
        loop.add(current_point)
        for move_x, move_y in moves[graph[current_point[1]][current_point[0]]]:
            new_point = (current_point[0] + move_x, current_point[1] + move_y)
            if len(loop) > 2 and new_point == starting_point:
                # starting point found after
                current_point = new_point
                break
            elif not new_point in loop:
                current_point = new_point
                break  # only 1 way to go through the pipes so we can break

    return loop


def get_part_one_solution(loop: set[tuple[int, int]]) -> str:
    return len(loop) // 2


# for part two,
# https://en.wikipedia.org/wiki/Pick%27s_theorem
# https://en.wikipedia.org/wiki/Jordan_curve_theorem or
# https://en.wikipedia.org/wiki/Flood_fill
# can be used.
def get_part_two_solution(graph: list[str], loop: set[tuple[int, int]]) -> str:
    total_area = 0
    for r in range(len(graph)):
        for c in range(len(graph[r])):
            if (c, r) in loop:
                continue

            crosses_count = 0

            cur_x, cur_y = c - 1, r - 1

            while cur_x >= 0 and cur_y >= 0:
                if (cur_x, cur_y) in loop:
                    char = graph[cur_y][cur_x]
                    if char != 'L' and char != '7':
                        crosses_count += 1
                cur_x -= 1
                cur_y -= 1

            if crosses_count % 2 == 1:
                total_area += 1

    return total_area


def main():
    graph = parse_input()
    starting_point = get_starting_point(graph)
    loop = get_loop_from_point(graph, starting_point)

    print(f"Solution 1: {get_part_one_solution(loop)}")
    print(f"Solution 2: {get_part_two_solution(graph, loop)}")


if __name__ == "__main__":
    main()

# 6717
