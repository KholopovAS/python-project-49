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
    return f"{num1} {operation} {num2}", result


def main(name=welcome_user()):


    while True:
        expression, correct_answer = generate_random_expression()  # присваивание значения работы функции 2м переменным.
        print(f"Question: {expression}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print(f'Congratulations, {name}')
            break
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again!")

if __name__ == "__main__":
    main()
