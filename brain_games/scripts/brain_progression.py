import random

from brain_games.cli import welcome_user

print("brain-progression\n")
name = welcome_user()


def generate_progression():
    length = random.randrange(5, 16)  # Генерируем длину от 5 до 15
    hidden_index = random.randrange(length)  # Выбираем случайную позицию для скрытого числа
    start = random.randrange(1, 100)  # Генерируем начальное значение
    diff = random.randrange(1, 10)  # Генерируем общую разницу
    progression = [start + i * diff for i in range(length)]  # Генерируем прогрессию
    progression[hidden_index] = ".."  # Заменяем скрытое число на две точки
    return progression, progression[
                            hidden_index] == "..", start + diff * hidden_index  # Возвращаем прогрессию и скрытое число


def main():
    while True:
        progression, is_hidden, correct_answer = generate_progression()
        print(" ".join(map(str, progression)))
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
            print(f"Congratulations, {name}!")
            break
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")


main()

if __name__ == "__main__":
    main()
