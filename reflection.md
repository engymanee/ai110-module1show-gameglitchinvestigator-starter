# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. **Backwards hints**
   - **Input/trigger:** I submitted any guess that was higher or lower than the secret number (for example, a guess of 80 when the secret was 50).
   - **Expected behavior:** A guess above the secret should say "Go LOWER!", and a guess below it should say "Go HIGHER!".
   - **Actual behavior:** The hint was always the opposite. A too-high guess told me to go higher, and a too-low guess told me to go lower.
   - **Code-level cause / location:** `check_guess` in `app.py`, lines 37-40. The `guess > secret` branch returns "Go HIGHER!" and the else branch returns "Go LOWER!", so the two messages are swapped.
2. **Secret number turns into a string on even attempts**
   - **Input/trigger:** Submitting a valid number on any attempt where the attempt counter is even (the counter is incremented before the check, so this includes my first guess).
   - **Expected behavior:** The guess is always compared to the secret as a number, so the hint is correct every time.
   - **Actual behavior:** On those attempts the secret was converted to a string, so the comparison fell back to text comparison and the hints were wrong (for example, "9" counts as greater than "50").
   - **Code-level cause / location:** The submit handler in `app.py`, lines 158-161: `if st.session_state.attempts % 2 == 0` calls `str()` on the secret. `check_guess` (lines 41-47) then hits its `TypeError` fallback and compares text instead of numbers.
3. **"Attempts left" label is one guess behind**
   - **Input/trigger:** Clicking "Submit Guess" for the first time, and then each guess after that.
   - **Expected behavior:** The label drops by one right after each guess (7 to 6 after the first guess on Normal difficulty).
   - **Actual behavior:** After the first guess the label still showed 7, so it looked like nothing happened. From the second guess on, it always showed the count from before my latest guess.
   - **Code-level cause / location:** `app.py`, lines 109-112 and 147-148. The `st.info(...)` label is drawn before the `if submit:` block runs `attempts += 1`, so each rerun displays the count from before the latest guess.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

1. **Attempts label does not update**
   - **Input:** Entered a number.
   - **Expected behavior:** The attempts label should decrease by one.
   - **Actual behavior:** The label still read 7.
   - **Console output / error:** N/A

2. **Out-of-range numbers are accepted**
   - **Input:** Entered 0 and -2.
   - **Expected behavior:** The game should prompt me to use only numbers between 1 and 100.
   - **Actual behavior:** Both numbers were accepted.
   - **Console output / error:** The game said "Go lower".

3. **"New Game" button does nothing**
   - **Input:** Clicked "New Game".
   - **Expected behavior:** The game should ask whether I really want to start over, then refresh once I accept.
   - **Actual behavior:** Nothing happened.
   - **Console output / error:** N/A

4. **Hints are backwards and wrong on some attempts**
   - **Input:** Guessed a number higher than the secret (e.g. 60 when the secret was 50), and later guessed on even-numbered attempts.
   - **Expected behavior:** A too-high guess should say "Go LOWER!" and a too-low guess should say "Go HIGHER!", on every attempt.
   - **Actual behavior:** The hints were swapped, and on every second attempt the hint was sometimes wrong even when the direction was right.
   - **Console output / error:** N/A (the `check_guess` tests also failed because the function returned a tuple instead of "Win" / "Too High" / "Too Low").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project. 
# I used Claude Enterprise
- Give one example of an AI suggestion that was correct: 
# when I was trying to fix the "New Game" button not doing anything ... I could not find the fucntion. I asked it for the function and it told me it was inline in app.py
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count
# Even though I had asked it to move the function parse_guess...it retained two instances... so i had to tell it to move it and only retain the call of the function

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
# I repeated the exact steps that caused the bug (like entering 0, or guessing too high) and checked the game behaved correctly. For the logic bugs I also ran pytest to confirm.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
# I ran test_guess_too_high (secret 50, guess 60 should give "Too High"). It failed at first because check_guess returned a tuple with a message instead of just the outcome. That showed me the function was doing two jobs, so I split the hint message into its own function.
- Did AI help you design or understand any tests? How?
# Yes. I gave it the failing tests and it explained why they failed, then fixed the code to match them.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
# Every time you click a button or type something, Streamlit re-runs the whole script from top to bottom, like refreshing the page. Normal variables get wiped on each run, so session state is the app's memory: anything stored there (the secret number, attempts, score) survives between reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
# Writing down the exact steps to reproduce a bug before asking AI to fix it, and having tests to check the fix afterward.
- What is one thing you would do differently next time you work with AI on a coding task?
# Ask to see the code before it is applied, and check the result myself instead of trusting that it did exactly what I asked.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
# AI generated code can look finished and still be full of bugs, so it needs testing and review like any other code. AI is a helpful teammate, but I'm still the one responsible for checking it.
