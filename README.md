# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Game purpose

Game Glitch Investigator is a number-guessing game built with Streamlit. The app picks a secret number within a range set, the player has a limited number of attempts to find it, and each guess gets a "Go HIGHER / Go LOWER" hint and updates a score. 

### Bugs found
1.  Backwards hints | A too-high guess said "Go HIGHER!" and a too-low guess said "Go LOWER!". Did not fix this
2.  Secret becomes a string on even attempts. Did not fix this  
3. "Attempts left" label is one guess behind  The label was drawn before the submit handler incremented the attempt counter, so it always showed the count from before the latest guess. 
4. Out-of-range numbers accepted. Guesses like 0 and -2 were accepted and got a hint instead of an error. 
5. "New Game" button did nothing. Clicking it did not reset the secret, score, attempts or history. 

### Fixes applied

- **Attempts label (bug 3):** moved the calculation into `attempts_left()` in `logic_utils.py`. `app.py` imports it and draws the label into a placeholder (`st.empty()`), then redraws it after the guess is processed so it shows the updated count.
- **Out-of-range guesses (bug 4):** moved `parse_guess` into `logic_utils.py` (only the import remains in `app.py`) and added `low`/`high` parameters. Guesses outside the difficulty's range are rejected with "Please enter a number between {low} and {high}." and no longer count as a valid guess.
- **New Game (bug 5):** clicking "New Game" now asks "Are you sure?". Confirming calls `reset_game()` in `logic_utils.py`, which picks a new secret, resets attempts, score, status and history, clears the input box, and shows "New Game Started". Cancel dismisses the prompt without changing anything.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!User enters a number -->
2. <!App checks if it is actually between 1 and 100 -->
3. <!User clicks on end game-->
4. <!App prompts the user to confirm they want to end and actually restarts -->
5. <!User enters a number -->
6. <!The label text accurately tells the user the actual number of steps -->


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
platform darwin -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/maneengozinnamani/Desktop/CodePath Projects/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 8 items                                                                                                                                                           

tests/test_game_logic.py ........                                                                                                                                     [100%]

============================================================================= 8 passed in 0.01s =============================================================================
maneengozinnamani@Mac ai110-module1show-gameglitchinvestigator-starter % 

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
