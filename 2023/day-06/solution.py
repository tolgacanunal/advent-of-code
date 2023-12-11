import os
import re
from typing import List, Tuple

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    time_raw, distance_raw = file_content.split("\n")
    race_data = [
        (int(r), int(c)) for r, c in
        zip(
            re.split(r'\s+', time_raw)[1:],
            re.split(r'\s+', distance_raw)[1:]
        )
    ]
    return race_data


# winning cases will be symmetrical in the middle of the time range.
# [LLL(L)WWWWWWLLLL] this is basically,
# trying to find a last (L) to figure out count of Ws in time range from [1..time)
def get_winning_count(time: int, distance: int) -> int:
    range_start = 1
    range_end = range_start + ((time - 1 - range_start) // 2)
    while range_start <= range_end:
        middle = (range_start + range_end) // 2
        race_time = time - middle
        if race_time * middle >= distance:
            range_end = middle - 1
        else:
            range_start = middle + 1
    return time - (range_end * 2) - 1


def get_part_one_solution(race_data: List[Tuple[int, int]]) -> str:
    result = 1
    for time, distance in race_data:
        result *= get_winning_count(time, distance)
    return result


def get_part_two_solution(race_data: List[Tuple[int, int]]) -> str:
    time_all_raw = ""
    distance_all_raw = ""
    for time, distance in race_data:
        time_all_raw += str(time)
        distance_all_raw += str(distance)
    time_all = int(time_all_raw)
    distance_all = int(distance_all_raw)
    return get_winning_count(time_all, distance_all)


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
