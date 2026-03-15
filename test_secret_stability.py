import random
import pytest
from app import get_range_for_difficulty


# Simulate the session-state secret logic from app.py:
#   if "secret" not in state or state["difficulty"] != difficulty:
#       state["secret"] = random.randint(low, high)
#       state["difficulty"] = difficulty

def generate_secret(state: dict, difficulty: str) -> dict:
    """Mirrors the session-state secret logic in app.py."""
    low, high = get_range_for_difficulty(difficulty)
    if "secret" not in state or state.get("difficulty") != difficulty:
        state["secret"] = random.randint(low, high)
        state["difficulty"] = difficulty
    return state


# --- Secret stays stable across multiple reruns ---

def test_secret_does_not_change_on_rerun():
    state = {}
    state = generate_secret(state, "Normal")
    first_secret = state["secret"]

    for _ in range(20):  # simulate 20 reruns
        state = generate_secret(state, "Normal")

    assert state["secret"] == first_secret, "Secret should not change across reruns"


def test_secret_stable_for_easy():
    state = {}
    state = generate_secret(state, "Easy")
    first_secret = state["secret"]
    for _ in range(20):
        state = generate_secret(state, "Easy")
    assert state["secret"] == first_secret


def test_secret_stable_for_hard():
    state = {}
    state = generate_secret(state, "Hard")
    first_secret = state["secret"]
    for _ in range(20):
        state = generate_secret(state, "Hard")
    assert state["secret"] == first_secret


# --- Secret regenerates when difficulty changes ---

def test_secret_resets_when_difficulty_changes():
    state = {}
    state = generate_secret(state, "Easy")
    state = generate_secret(state, "Normal")  # difficulty changed
    assert state["difficulty"] == "Normal"
    low, high = get_range_for_difficulty("Normal")
    assert low <= state["secret"] <= high


# --- New secret is always within the correct range ---

def test_secret_within_easy_range():
    for _ in range(50):
        state = generate_secret({}, "Easy")
        assert 1 <= state["secret"] <= 20, f"Easy secret {state['secret']} out of range"


def test_secret_within_normal_range():
    for _ in range(50):
        state = generate_secret({}, "Normal")
        assert 1 <= state["secret"] <= 100, f"Normal secret {state['secret']} out of range"


def test_secret_within_hard_range():
    for _ in range(50):
        state = generate_secret({}, "Hard")
        low, high = get_range_for_difficulty("Hard")
        assert low <= state["secret"] <= high, f"Hard secret {state['secret']} out of range"
