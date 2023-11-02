import os
import heapq

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")

def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    return file_content

def get_part_one_solution(input) -> str:
    splitted_calories = input.split(os.linesep)
    i = 0
    sum = 0
    max_sum = 0
    while i < len(splitted_calories):
        if splitted_calories[i] == '':
            max_sum = max(sum, max_sum)
            sum = 0
        else:
            sum += int(splitted_calories[i])
        i += 1
        
    return max_sum

def get_part_two_solution(input) -> str:
    splitted_calories = input.split(os.linesep)
    top_3 = []
    i = 0
    sum_elf = 0
    while i < len(splitted_calories):
        if splitted_calories[i] == '':
            heapq.heappush(top_3, sum_elf)
            if len(top_3) > 3:
                heapq.heappop(top_3)
            sum_elf = 0
        else:
            sum_elf += int(splitted_calories[i])
        i += 1
        
    return sum(top_3)

def main():
    input = parse_input()
    print(f"Solution 1: {get_part_one_solution(input)}")
    print(f"Solution 2: {get_part_two_solution(input)}")

if __name__ == "__main__":
    main()
