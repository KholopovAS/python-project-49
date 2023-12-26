import random

from brain_games.cli import welcome_user


def generate_random_expression():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 10)  # генерация значения переменно num1
    num2 = random.randint(1, 10)  # генерация значения переменно num2
    operation = random.choice(operations)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    return print(f"Question: {num1} {operation} {num2}"), result


def main(name=welcome_user()):
    score = 0  # Инициализация счетчика
    print("What is the result of the expression?")
    while True:
        expression, correct_answer = generate_random_expression()
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print(f'Correct!')
            score += 1  # Увеличение счетчика
            if score >= 3:  # Проверка, достигли ли мы трех правильных ответов
                print(f'Congratulations, {name}!')
                break
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
