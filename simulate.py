import random
from game_logic import check_guess, generate_secret_code
from mastermindbot import MastermindBot

def simulate_games(simulations=100):
    total_attempts = 0

    for _ in range(simulations):
        secret_code = generate_secret_code(4, 8)
        bot = MastermindBot(4, 8)
        history = []
        attempts = 0

        while attempts < 10:
            if not history:
                guess = [random.randint(0, 7) for _ in range(4)]
            else:
                guess = bot.get_hint(history)
            
            correct_pos, correct_num = check_guess(secret_code, guess)
            history.append((guess, (correct_pos, correct_num)))
            attempts += 1

            if correct_pos == 4:
                break

        total_attempts += attempts

    average_attempts = total_attempts / simulations
    print(f"Average attempts over {simulations} games: {average_attempts}")

if __name__ == "__main__":
    simulate_games()
