# Mastermind Game by Jaeschel Acheampong

This is the REACH Mastermind Game, designed as a command-line game where players try to guess a secret number combination within 10 attempts. The game showcases backend engineering principles, including API integration, game logic, and input validation.

## Project Overview
The Mastermind Game demonstrates problem-solving as a backend engineer by tackling core challenges such as input validation, API integration, and efficient search algorithms through a hint-generating bot. This README reflects my thought process, decisions made, and future improvements.

---

## Getting Started

### Prerequisites
- Python 3.8+
- `requests` library (for API integration)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mastermind-game
   ```

2. Install the required packages:
   ```bash
   pip install requests
   ```

---

## Running the Game
1. Run the game using:
   ```bash
   python main.py
   ```

2. To quit the game:
   - On Mac: Press `Ctrl+C`
   - On Windows: Press `Ctrl+C`
   - On Linux: Press `Ctrl+C`

---

## How to Play
- The computer randomly selects a 4-number combination from digits `0-7` (duplicates allowed).
- You have 10 attempts to guess the correct combination.
- After each guess, you receive feedback:
  - **Correct number, wrong location**
  - **Correct number and correct location**
  - **All numbers incorrect**

### Example Run
```
Number of attempts left: 10
Enter your 4-number guess: 1234
Feedback: 1 correct number, 1 correct location
```

---

## Game Features
- **Custom Game Settings**: Configure the game with your preferred code length and digit range.
- **Hint System**: A bot provides a best-guess hint if you are stuck.
- **Play Again**: A system that resets gameplay.

---

## Tests
To run the tests:
```bash
python -m unittest discover
```
### Test Areas
- **Game Logic**: Code generation, feedback evaluation.
- **Input Validation**: Cleaning up guesses and validating inputs.
- **Bot Behavior**: Filtering guesses and providing accurate hints.
- **API Fallback**: Ensures the game runs even if the API is unavailable.

---

## Future Improvements
- **Multiplayer Game**: Ask for someone else's secret code.
- **Leave Game**: Add a "clean" exit option during gameplay.

---

## Abandoned Ideas
- **MastermindSmart**: A smarter way to make a predictive guess.
    - This idea was abandoned due to high time complexity causing performance issues.
    - Isn't effective enough to be worth it
- **Lucky Break**: After 5 guesses, reveal one correct number and position.
    - Although I couldn't implement this feature due to time constraints, its logic is well-defined:
        - In `main.py`, initialize a variable `lucky_guess = False`.
        - Add a conditional check: `if attempts <= 5 and not lucky_guess:` prompt the user if they want to use a lucky guess.
        - If the user agrees, reveal one correct number and its position in the secret code, then set `lucky_guess = True` to prevent reuse for the rest of the game.


---

## Thought Process
Throughout development, I focused on ensuring:
- **Modular Design**: Functions and classes are well-organized and reusable.
- **Robust Error Handling**: Proper fallbacks and clear error messages.
- **User Experience**: Clear instructions and dynamic feedback.

For each feature implementation, my approach centered on breaking down the functionality into its smallest components and building from the ground up. This foundational-first strategy ensured that each part of the system was structurally sound before scaling or optimizing further. By focusing on core logic early on, I could address potential edge cases, simplify debugging, and maintain clean, modular code. This method allowed for more efficient optimization later in the development process while ensuring that each feature remained robust, maintainable, and extensible.

### Challenges
During this process, one of the most challenging aspects I encountered was error testing. My background in Biomedical and Mechanical Engineering involved working extensively with standard data formats such as JSON, CSV, and TXT files. As a result, much of my previous experience centered around data cleaning, smoothing, and presentation. Transitioning to a backend development environment required adapting these skills to a new context, where managing dynamic data structures and ensuring robust error handling became critical components of the development process. This shift deepened my understanding of data integrity and system reliability from an engineering perspective.

By documenting this process, I aim to reflect the mindset of a backend engineer solving a challenging game logic problem.

---

**Thanks for Playing!**

Last Editied December 12th, 2024