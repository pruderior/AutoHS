from card.basic_card import *
from typing import Optional


def get_card_in_hand(card: Card, state):
    for c in state.my_hand_cards:
        if c.card_id == card.id:
            return c
    return None


def get_current_mana(state) -> int:
    return state.my_last_mana


def can_play_card(card: Card, mana: int, state) -> bool:
    cardEntity = get_card_in_hand(card, state)
    if cardEntity is None:
        return False
    return cardEntity.get_cost <= mana
