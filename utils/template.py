import os

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    return file_content


def get_part_one_solution(input) -> str:
    return "not solved yet."


def get_part_two_solution(input) -> str:
    return "not solved yet."


def main():
    input = parse_input()
    print(f"Solution 1: {get_part_one_solution(input)}")
    print(f"Solution 2: {get_part_two_solution(input)}")


if __name__ == "__main__":
    main()
