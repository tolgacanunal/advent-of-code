import os
import re
from collections import defaultdict
from typing import Set, Tuple

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


def parse_input() -> list[Tuple[Set[str], Set[str]]]:
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    regexed_content = re.sub(r'Card \d+: ', '', file_content)
    card_list = regexed_content.split("\n")
    return [parse_card_raw(c_raw) for c_raw in card_list]


def parse_card_raw(card_raw: str) -> Tuple[Set[str], Set[str]]:
    winning_cards_raw, players_card_raw = card_raw.split(" | ", maxsplit=1)
    winning_cards = set(winning_cards_raw.split(" "))
    player_cards = set(players_card_raw.split(" "))
    winning_cards.discard('')
    player_cards.discard('')
    return (winning_cards, player_cards)


def get_part_one_solution(parsed_card_list: list[Tuple[Set[str], Set[str]]]) -> str:
    total_prize = 0
    for winning_cards, players_cards in parsed_card_list:
        prize = 0
        for p_card in players_cards:
            if p_card in winning_cards:
                prize = 1 if prize == 0 else prize * 2
        total_prize += prize
    return total_prize


def get_part_two_solution(parsed_card_list: list[Tuple[Set[str], Set[str]]]) -> str:
    total_count = 0
    scratch_card_count_list = [1 for _ in range(len(parsed_card_list))]
    for index, (winning_cards, players_cards) in enumerate(parsed_card_list):
        multiplier = scratch_card_count_list[index]
        winning_count = len(players_cards.intersection(winning_cards))
        for i in range(min(winning_count, len(parsed_card_list))):
            scratch_card_count_list[index + 1 + i] += multiplier
        total_count += scratch_card_count_list[index]
    return total_count


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
