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
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
