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


def get_hold_times_for_record(time, distance):
    possible_hold_times = range(1, time)
    possible_ways = 0
    for pht in possible_hold_times:
        race_time = time - pht
        if (pht * (race_time)) > distance:
            possible_ways += 1
    return possible_ways


def get_part_one_solution(race_data: List[Tuple[int, int]]) -> str:
    result = 1
    for time, distance in race_data:
        result *= get_hold_times_for_record(time, distance)
    return result


def get_part_two_solution(race_data: List[Tuple[int, int]]) -> str:
    time_all_raw = ""
    distance_all_raw = ""
    for time, distance in race_data:
        time_all_raw += str(time)
        distance_all_raw += str(distance)
    time_all = int(time_all_raw)
    distance_all = int(distance_all_raw)
    return get_hold_times_for_record(time_all, distance_all)


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
