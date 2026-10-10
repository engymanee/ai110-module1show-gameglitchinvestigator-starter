import random

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
 
  # Fix: moved parse_guess here from app.py and added low/high range parameters so
    # guesses outside the difficulty range (e.g. 0 or -2) are rejected with an error message 
    # I selected the bug description in the reflection.md document and told it to
    # go pick the function in app.py and move it here and ensure that only numbers
    # between 1 to 100 are accepted.

def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Please enter a number between {low} and {high}."

    return True, value, None


# Fix: the "Attempts left" label was computed inline in app.py and drawn before the
# submit handler incremented st.session_state.attempts, so it always showed the old
# value. I aske Ai to move the function here but it explained to me a better way
#  the calculation here (removed it from app.py) and app.py now draws
# the label into a placeholder again after the guess is processed.

def attempts_left(attempt_limit: int, attempts_used: int) -> int:
    """Return how many attempts remain (never below zero)."""
    return max(attempt_limit - attempts_used, 0)


# Fix: check_guess was moved here from app.py. Three bugs were fixed:
# 1) the hints were backwards (a too-high guess said "Go HIGHER!"), so they now
#    say "Go LOWER!" for a too-high guess and "Go HIGHER!" for a too-low guess;
# 2) it now returns only the outcome string ("Win" / "Too High" / "Too Low") so it
#    matches the tests, and the message comes from get_hint();
# 3) the str() fallback that compared guesses as text (so "9" > "50") was removed,
#    because the secret is always an int now.
# I selected the failing tests and asked AI to fix the function, move it here and
# import it in app.py.

def check_guess(guess: int, secret: int) -> str:
    """
    Compare guess to secret and return the outcome.

    outcome: "Win", "Too High", or "Too Low"
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def get_hint(outcome: str) -> str:
    """Return the player-facing hint message for an outcome."""
    hints = {
        "Win": "🎉 Correct!",
        "Too High": "📉 Go LOWER!",
        "Too Low": "📈 Go HIGHER!",
    }
    return hints.get(outcome, "")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# FIXME: Logic breaks here

#Fix: I asked AI to make New Game ask "are you sure?" first, then reset the counters,
# status and everything else, show "New Game Started", and move it into logic_utils.py.

def reset_game(state, low: int, high: int, difficulty: str):
    """Reset all game state for a fresh round and flag the 'New Game Started' message."""
    state.secret = random.randint(low, high)
    state.attempts = 1
    state.score = 0
    state.status = "playing"
    state.history = []
    state[f"guess_input_{difficulty}"] = ""
    state.confirm_new_game = False
    state.just_reset = True
