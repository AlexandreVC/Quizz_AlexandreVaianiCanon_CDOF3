import requests
import html
import random

def get_questions(amount=20):
    url = f"https://opentdb.com/api.php?amount=20"
    response = requests.get(url)
    questions = response.json()['results']
    return [(html.unescape(q['question']), html.unescape(q['correct_answer']),
             [html.unescape(a) for a in q['incorrect_answers']]) for q in questions]

def quiz_game():
    questions = get_questions()
    score = 0
    lives = 3

    for i, (question, correct_answer, incorrect_answers) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        options = [correct_answer] + incorrect_answers
        random.shuffle(options)

        for idx, option in enumerate(options, 1):
            print(f"{idx}: {option}")

        try:
            user_answer = int(input("Your answer (1-4): "))
            if options[user_answer - 1] == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was '{correct_answer}'.")
                lives -= 1
                print(f"You have {lives} lives left")
                if lives == 0:
                    print("\nYou've run out of lives. Game over!")
                    break
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 4.")

    print(f"\nYour score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
