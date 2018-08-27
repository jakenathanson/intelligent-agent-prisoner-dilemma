"""Utilities used by various strategies"""
import itertools
from functools import lru_cache

from gamesimulator.player import update_history
from gamesimulator.action import Action


A, B = Action.A, Action.B


def detect_cycle(history, min_size=1, max_size=12, offset=0):
    """Detects cycles in the sequence history.

    Mainly used by hunter strategies.

    Parameters
    ----------
    history: sequence of A and B
        The sequence to look for cycles within
    min_size: int, 1
        The minimum length of the cycle
    max_size: int, 12
    offset: int, 0
        The amount of history to skip initially
    """
    history_tail = history[offset:]
    new_max_size = min(len(history_tail) // 2, max_size)
    for i in range(min_size, new_max_size + 1):
        has_cycle = True
        cycle = tuple(history_tail[:i])
        for j, elem in enumerate(history_tail):
            if elem != cycle[j % len(cycle)]:
                has_cycle = False
                break
        if has_cycle:
            return cycle
    return None


def limited_simulate_play(player_1, player_2, h1):
    """Here we want to replay player_1's history to player_2, allowing
    player_2's strategy method to set any internal variables as needed."""
    h2 = inspect_strategy(player_1, player_2)
    update_history(player_1, h1)
    update_history(player_2, h2)


def simulate_match(player_1, player_2, strategy, rounds=10):
    """Simulates a number of matches."""
    for match in range(rounds):
        limited_simulate_play(player_1, player_2, strategy)


def calculate_scores(p1, p2, game):
    """Calculates the score for two players based their history"""
    s1, s2 = 0, 0
    for pair in zip(p1.history, p2.history):
        score = game.score(pair)
        s1 += score[0]
        s2 += score[1]
    return s1, s2
