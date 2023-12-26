import random

from brain_games.cli import welcome_user

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print("brain-gcd\n")
name = welcome_user()


def main():
    print("Find the greatest common divisor of given numbers.")
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f"Question: {num1} {num2}")
    user_answer = int(input('Your answer: '))
    correct_answer = gcd(num1, num2)
    if user_answer == correct_answer:
        print(f"Correct!\nCongratulations, Sam!\n")
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
