rfrom logic_utils import check_guess, parse_guess, reset_game

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# Bug 1: parse_guess accepted numbers outside the difficulty range (e.g. 0, -2, 101)
def test_parse_guess_rejects_out_of_range():
    for raw in ["0", "-2", "101"]:
        ok, value, err = parse_guess(raw, 1, 100)
        assert not ok
        assert value is None
        assert "between 1 and 100" in err

def test_parse_guess_accepts_in_range_bounds():
    assert parse_guess("1", 1, 100) == (True, 1, None)
    assert parse_guess("100", 1, 100) == (True, 100, None)


# Bug 2: New Game only reset attempts/secret and ignored the difficulty range
class FakeState(dict):
    """Mimics st.session_state: supports both attribute and key access."""
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

def test_reset_game_refreshes_everything():
    state = FakeState(secret=999, attempts=7, score=45, status="lost",
                      history=[1, 2, 3], confirm_new_game=True)
    state["guess_input_Easy"] = "15"

    reset_game(state, 1, 20, "Easy")

    assert 1 <= state.secret <= 20
    assert state.attempts == 1
    assert state.score == 0
    assert state.status == "playing"
    assert state.history == []
    assert state["guess_input_Easy"] == ""
    assert state.confirm_new_game is False
    assert state.just_reset is True
