from collections import Counter
from functools import cache
import os
from typing import List, Literal

INPUT_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "input")


def parse_input():
    with open(INPUT_FILE_LOCATION, "r") as input_file:
        file_content = input_file.read()
    game: List[tuple[str, str]] = []
    for line in file_content.split("\n"):
        hand, bid = line.split(" ")
        game.append((hand, bid))
    return game


@cache
def get_card_rank(card: str, is_joker_included: bool) -> int:
    if card == 'A':
        return 14
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'J':
        return 1 if is_joker_included else 11
    elif card == 'T':
        return 10
    else:
        return int(card)


@cache
def compare_card_in_same_category(card: str, card_other: str, is_joker_included: bool) -> Literal[-1, 1, 0]:
    # 1 -> win 0 -> equal  -1 -> lose
    for index in range(len(card)):
        if card[index] != card_other[index]:
            card_rank = get_card_rank(card[index], is_joker_included)
            other_card_rank = get_card_rank(
                card_other[index], is_joker_included)
            if card_rank < other_card_rank:
                return -1
            else:
                return 1
    return 0


# This part can be cleaned up with Enums.
def get_category(hand: str, is_joker_included: bool):
    hand_counter = Counter(hand)

    if is_joker_included and 'J' in hand_counter.keys() and len(hand_counter.keys()) > 1:
        joker_count = hand_counter['J']
        most_common_char_other_than_J = list(
            filter(lambda x: x[0] != 'J', hand_counter.most_common(2))
        )[0][0]
        del hand_counter['J']
        hand_counter[most_common_char_other_than_J] += joker_count

    category = None

    if len(hand_counter.keys()) == 1:
        category = 6  # five of a kind
    elif len(hand_counter.keys()) == 2:
        if hand_counter.most_common(1)[0][1] == 4:
            category = 5  # four of a kind
        else:
            category = 4  # full house
    elif hand_counter.most_common(1)[0][1] == 3:
        category = 3  # three of a kind
    elif len(hand_counter.keys()) == 3:
        category = 2  # two pair
    elif len(hand_counter.keys()) == 4:
        category = 1  # one pair
    else:
        category = 0  # high card

    assert (category != None)

    return category


def get_total_bid(game: list[tuple[str, str]], is_joker_included: bool) -> int:
    categories: list[list[tuple[str, str]]] = [[] for _ in range(7)]
    for hand, bid in game:
        category = get_category(hand, is_joker_included=is_joker_included)
        categories[category].append((hand, bid))

    bid_total = 0
    rank = 1
    for category in categories:
        for rank_checked_hand, rank_checked_bid in category:
            winning_count = 0
            for compared_hand, _ in category:
                if compared_hand == rank_checked_hand:
                    continue
                if compare_card_in_same_category(rank_checked_hand, compared_hand, is_joker_included) == 1:
                    winning_count += 1
            bid_total += int(rank_checked_bid) * (rank + winning_count)
        rank += len(category)

    return bid_total


def get_part_one_solution(game: list[tuple[str, str]]) -> str:
    return get_total_bid(game=game, is_joker_included=False)


def get_part_two_solution(game: list[tuple[str, str]]) -> str:
    return get_total_bid(game=game, is_joker_included=True)


def main():
    s = parse_input()
    print(f"Solution 1: {get_part_one_solution(s)}")
    print(f"Solution 2: {get_part_two_solution(s)}")


if __name__ == "__main__":
    main()
