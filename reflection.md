# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looks normal visually when you run it for the first time. It is functional in the sense that all buttons work and it takes in an integer input, you can win by guessing correctly, etc.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The constraints say that you need to be between 1-100, but if you give a number outside those constraints it still accepts it.
  2. The higher/lower hints are flipped. For example, if the answer is 80 and I guess 75 the hint will say "Go Lower" and vice versa if I guessed 85 it would say "Go Higher".

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I was trying to fix problem 2 I listed above. Claude suggested the error was on even-numbered attempts, the hint direction can be completely wrong because it's doing alphabetical string comparison instead of numeric comparison.
When prompting further after the first fix did not work, Claude swapped lines 37 and 40 as the messages were swapped. I verified the result by running the app again and testing the hint messages to get the correct results.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

When asking about the reward point system, Claude originally said that both update_score "Too High" and "Too Low" had errors in point distribution. However after examining and running the code, this was incorrect. Only the Too High logic was incorrect. After asking Claude about the mistake it re-framed to only fix "Too High". I think part of the issue was me not explaining the game mechanics properly before asking it to fix the point system.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Both manually by fixing logic and then running the game to see the change and I had Claude write a test file.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran test_game_logic.py in the tests folder and passed all 12 tests. This was a test file Claude wrote after fixing the mistake witht he point system logic after some prompting. It covers both "Too high" and "Too low" logic and unkown/empty outcomes.
- Did AI help you design or understand any tests? How?
Yes Claude built the test file described above after giving me an incorrect fix to the scoring logic. Claude made sure to fix the mistake and instead of only testing the vald point system error, it also tested the error it had fixed to show that logic was working as well. After making the test file I allowed Claude to run it for me and explain every passed testcase.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Every time you interact with a Streamlit app, Streamlit reruns the entire script from top to bottom. Without session state, `random.randint()` would be called fresh on every rerun, generating a new secret number each time. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Everytime you do anything in Streamlit, it "reruns" the entire script from top to bottom or in other words it starts fresh without remembering where it was. Session state is a way for Streamlit to remember value that should "survive" the reruns. Without session state (like in this case), the secret number value would execute on every single rerun, picking a brand new secret number every time the user interacted with the page.
- What change did you make that finally gave the game a stable secret number?
Two things changed: 1. Saving the difficulty and the random secret number to session_state to fix the number getting wrote over. 2. adding a difficulty check when you switch difficulties.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
