from dataclasses import dataclass
import os
from random import seed
from typing import Callable, Dict, List, Self, Set, Tuple

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


class MapItem:
    def __init__(self, destination_range_start: int, source_range_start: int, range_length: int):
        self.source_range = range(
            source_range_start, source_range_start + range_length)
        self.difference = destination_range_start - source_range_start


def parse_input() -> tuple[List[int], List[List[MapItem]]]:
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    splitted_text = file_content.split("\n\n")
    seed_raw, map_raw_list = splitted_text[0], splitted_text[1:]

    seeds = seed_raw.split(" ")[1:]

    map_steps = []
    for map_raw in map_raw_list:
        map_items = []
        splitted_map_raw = map_raw.split("\n")
        values = splitted_map_raw[1:]
        for v in values:
            destination_range_start, source_range_start, range_length = map(
                int, v.split(" "))

            map_items.append(
                MapItem(
                    destination_range_start,
                    source_range_start,
                    range_length
                )
            )
        map_steps.append(map_items)

    return (seeds, map_steps)


def get_part_one_solution(data: tuple[List[str], List[List[MapItem]]]) -> str:
    seeds_raw, map_steps = data
    min_location = 10**15

    for s_raw in seeds_raw:
        current_value = int(s_raw)
        for map_step in map_steps:
            for map_item in map_step:
                if current_value in map_item.source_range:
                    current_value += map_item.difference
                    break
        min_location = min(min_location, current_value)

    return min_location


def get_part_two_solution(data: tuple[List[str], List[List[MapItem]]]) -> str:
    seeds_raw, map_steps = data
    min_location = 10**15

    for s_index in range(0, len(seeds_raw), 2):
        start = int(seeds_raw[s_index])
        count = int(seeds_raw[s_index + 1])
        ranges: Set[Tuple[int, int]] = {(start, start + count - 1)}
        for map_step in map_steps:
            temp_ranges = set()
            for map_item in map_step:
                pass
            ranges = temp_ranges
        min_location = min(min_location, sorted(
            ranges, key=lambda x: x[0])[0][0])

    return min_location


def main():
    s: tuple[List[int], List[List[MapItem]]] = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
