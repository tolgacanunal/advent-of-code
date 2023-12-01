import os
import re

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")
WORD_TO_NUM = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    return file_content

def get_part_one_solution(s) -> str:
    regexed_input = re.sub(r'[^0-9\n]+', '', s.strip())
    splitted_input = regexed_input.split("\n")
    mapped_input = map(lambda x: int(x[0] + x[-1]), splitted_input)
    return sum(mapped_input)

def get_part_two_solution(s) -> str:
    for k,v in WORD_TO_NUM.items():
        s = s.replace(k, f"{k}{v}{k}") # trick to not miss overlapped number string.
    return get_part_one_solution(s)

def main():
    input = parse_input()
    print(f"Solution 1: {get_part_one_solution(input)}")
    print(f"Solution 2: {get_part_two_solution(input)}")


if __name__ == "__main__":
    main()
