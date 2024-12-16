## REACH BACKEND INTERVIEW UPDATES

**Requirement**: 
   - Allow users to choose what range of contiggous digits they can choose from.

**Design Logic**:
   -  User Input Configuration: Prompt the user for the max/min digits and validate it
   -  Code Generation: Use specified range to generate the secret code
   -  Guess Validaton: Validate that the user guess matches the new digit range
   -  Game Integration: Ensure the game loop works

**Implementation**: 
   - Configuring game settings through user input generating the secret code within the specified range, and ensuring all guesses are validated accordingly. The hint system and feedback logic also need to respect these settings

**Test**:
   - Correct handling of various digit range configurations.
   - Validation of guesses within and outside the configured range.
   - Feedback for all edge cases, including maximum and minimum digit values.


# Mastermind Game by Jaeschel Acheampong

This is the REACH Mastermind Game, designed as a command-line game where players try to guess a secret number combination within 10 attempts. The game showcases backend engineering principles, including API integration, game logic, and input validation.

## Project Overview
The Mastermind Game demonstrates problem-solving as a backend engineer by tackling core challenges such as input validation, API integration, and search algorithms through a hint-generating bot. This README reflects my thought process, decisions made, and future improvements.

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

Number of attempts left: 9
Enter your 4-number guess: 1301
Feedback: 2 correct numbers, 1 correct location

Number of attempts left: 8
Enter your 4-number guess: 1312
Feedback: You've Guessed the Code Correctly!
```

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
## Game Requirements
- **Code API Generation**: Ability to generate a secret code from "https://www.random.org"
- **4 Digit Guesses**: Ability to guess the combinations of 4 numbers
- **History of Guesses and Feedback**: Ability to view the history of guesses and their feedback 
- **Number of Attempts**: The number of guesses remaining is displayed

## Extension Features
- **Custom Game Settings**: Configure the game with your preferred code length and digit range.
- **Hint System**: A bot provides a best-guess hint if you are stuck.

---

## File Usage
- **main.py**: Main Mastermind gameplay.
- **game_logic**: Implements the core game logic, including code generation and guess evaluation.
- **game_settings**: Manages customizable game settings.
- **mastermindbot.py**: defines a bot that provides hints based on past attempts.
- **tools.py**: Provides utility functions for input validation, cleaning guesses, and displaying guess history.
- **test.py**: Contains extensive unit tests to validate the correctness of game logic, bot behavior, and input handling.

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

## Future Imporvement/Abandoned Ideas

- **Game Modes**: allowing the user different options of gameplay difficulty.
    - Time just prevented implementation
    - The general idea would be to prompt the user for a difficulty level (easy/standard/hard/custom)
       - **"easy"** would be a 3 digit game, with 4 digit options
       - **"standard"** would be the standard 4 digit game with 8 options
       - **"hard"** would be a 6 digit game with 8 options
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
One of the main challenges I faced during this project was transitioning from a biomedical/mechanical engineering mindset to a programmer's mindset. In my previous work, I was primarily focused on data processing, cleaning, and analysis. These tasks didn’t require as much emphasis on modularization, readability, or long-term code maintainability.

However, building this project required me to adopt best practices in software development, including designing reusable functions, structuring code into clear modules, and writing tests. Shifting from focusing solely on immediate data outputs to considering how well the code is organized and how easily it can be understood by others was a significant adjustment. This mindset shift taught me valuable lessons about scalable and maintainable coding practices that I will carry forward into future projects.

---

**Thanks for Playing!**

Last Editied December 12th, 2024