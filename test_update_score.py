import pytest
from app import update_score


# --- Win outcome ---

def test_win_first_attempt():
    # attempt 1: points = 100 - 10 * (1 + 1) = 80
    assert update_score(0, "Win", 1) == 80

def test_win_later_attempt():
    # attempt 5: points = 100 - 10 * (5 + 1) = 40
    assert update_score(0, "Win", 5) == 40

def test_win_minimum_points():
    # attempt 10: 100 - 10 * 11 = -10 → clamped to 10
    assert update_score(0, "Win", 10) == 10

def test_win_adds_to_existing_score():
    assert update_score(50, "Win", 1) == 130  # 50 + 80


# --- Too High outcome ---

def test_too_high_deducts_5_on_even_attempt():
    assert update_score(100, "Too High", 2) == 95

def test_too_high_deducts_5_on_odd_attempt():
    assert update_score(100, "Too High", 3) == 95

def test_too_high_always_deducts_5_regardless_of_attempt():
    for attempt in range(1, 10):
        assert update_score(100, "Too High", attempt) == 95, (
            f"Expected 95 on attempt {attempt}, got {update_score(100, 'Too High', attempt)}"
        )


# --- Too Low outcome ---

def test_too_low_deducts_5():
    assert update_score(100, "Too Low", 1) == 95

def test_too_low_deducts_5_multiple_attempts():
    for attempt in range(1, 10):
        assert update_score(100, "Too Low", attempt) == 95


# --- Symmetry: Too High and Too Low behave the same ---

def test_too_high_and_too_low_symmetric():
    for attempt in range(1, 10):
        assert update_score(100, "Too High", attempt) == update_score(100, "Too Low", attempt), (
            f"Too High and Too Low should deduct the same on attempt {attempt}"
        )


# --- Unknown outcome ---

def test_unknown_outcome_no_change():
    assert update_score(50, "Unknown", 1) == 50

def test_empty_outcome_no_change():
    assert update_score(50, "", 1) == 50
