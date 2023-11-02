import os
import heapq

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")

def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    return file_content.strip().split(os.linesep)

def get_part_one_solution(splitted_data: list[str]) -> str:
    sum_elf = 0
    max_sum_calories = 0
    for each_line in splitted_data:
        if each_line == '':
            max_sum_calories = max(sum_elf, max_sum_calories)
            sum_elf = 0
        else:
            sum_elf += int(each_line)
        
    return max_sum_calories

def get_part_two_solution(splitted_data: list[str]) -> str:
    top_list = []
    sum_elf = 0
    for each_line in splitted_data:
        if each_line == '':
            heapq.heappush(top_list, sum_elf)
            if len(top_list) > 3:
                heapq.heappop(top_list)
            sum_elf = 0
        else:
            sum_elf += int(each_line)

    return sum(top_list)

def main():
    input = parse_input()
    print(f"Solution 1: {get_part_one_solution(input)}")
    print(f"Solution 2: {get_part_two_solution(input)}")

if __name__ == "__main__":
    main()
