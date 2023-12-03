import os
import argparse
import shutil
import requests

MAIN_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__),  '..'))
TEMPLATE_FILE_LOC = os.path.join(os.path.dirname(__file__),  'template.py')

parser = argparse.ArgumentParser(
    prog="Day Fetcher for Advent of Code",
    description="Fetching all data needed for a day in advent of code event",
    epilog=""
)

parser.add_argument("year")
parser.add_argument("day")


def fetch_day_input(cookie: str, day: str, year: str) -> str:
    return requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers={"Cookie": cookie}).text


def main():
    cookie = os.environ.get('AOC_COOKIE')
    assert (cookie)

    args = parser.parse_args()
    day, year = args.day, args.year

    folder = f"{MAIN_FOLDER}/{year}/day-{day}"

    if os.path.exists(folder):
        print("Day already exists")
        return

    os.makedirs(folder)

    content = fetch_day_input(cookie, day, year)

    with open(f"{folder}/input", "w") as input_file:
        input_file.write(content)

    shutil.copyfile(TEMPLATE_FILE_LOC, f"{folder}/solution.py")

    print(f"AOC - {day}/{year} files are added")


if __name__ == "__main__":
    main()
