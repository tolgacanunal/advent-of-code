import os
from typing import Set, Tuple

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    return file_content


def is_block_part(lines: list[str], start: int, end: int, vertical_pos: int) -> bool:
    for v in range(max(0, vertical_pos - 1), min(len(lines), vertical_pos + 2)):
        for h in range(max(0, start - 1), min(len(lines[v]), end + 1)):
            character = lines[v][h]
            if not character.isdigit() and not character == '.':
                return True
    return False


def get_part_one_solution(s: str) -> int:
    lines: list[str] = s.split("\n")
    total = 0
    for lines_v_pos, line_raw in enumerate(lines):
        characters_in_line = len(line_raw)
        cur_h_pos = 0
        digit_start_pos = None
        while cur_h_pos <= characters_in_line:
            is_pos_at_the_end = cur_h_pos == characters_in_line
            if not is_pos_at_the_end and line_raw[cur_h_pos].isdigit():
                if digit_start_pos == None:
                    digit_start_pos = cur_h_pos
            elif digit_start_pos != None:
                if is_block_part(lines, digit_start_pos, cur_h_pos, lines_v_pos):
                    total += int(line_raw[digit_start_pos:cur_h_pos])
                digit_start_pos = None
            cur_h_pos += 1
    return total


def get_adjacent_numbers_from_pos(lines: list[str], x: int, y: int) -> list[int]:
    all_numbers = []
    visited_points: Set[Tuple[int, int]] = set()
    for y_pos in range(max(0, y - 1), min(len(lines), y + 2)):
        for x_pos in range(max(0, x - 1), min(len(lines[0]), x + 2)):
            if (x_pos, y_pos) in visited_points:
                continue
            visited_points.add((x_pos, y_pos))
            character = lines[y_pos][x_pos]
            if character.isdigit():
                start_index = x_pos
                end_index = x_pos
                while start_index > 0 and lines[y_pos][start_index].isdigit():
                    start_index -= 1
                    visited_points.add((start_index, y_pos))
                while end_index < len(lines[0]) and lines[y_pos][end_index].isdigit():
                    visited_points.add((end_index, y_pos))
                    end_index += 1
                all_numbers.append(
                    int(lines[y_pos][start_index + 1:end_index])
                )
    return all_numbers


def get_part_two_solution(s: str) -> str:
    lines: list[str] = s.split("\n")
    gear_sums = 0

    for lines_v_pos, line_raw in enumerate(lines):
        characters_in_line = len(line_raw)
        cur_h_pos = 0
        while cur_h_pos < characters_in_line:
            if line_raw[cur_h_pos] == '*':
                res = get_adjacent_numbers_from_pos(
                    lines, cur_h_pos, lines_v_pos
                )
                if len(res) == 2:
                    gear_sums += res[0] * res[1]
            cur_h_pos += 1
    return gear_sums


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
