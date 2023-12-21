import random

from brain_games.cli import welcome_user

def game1(name):

    i = 0 # счетчик правильных ответов
    print('Answer "yes" if the number is even, otherwise answer "no"')
    while i < 3:
        n = random.randint(0, 100)
        print(f'{"Question:"} {n}')
        user_answer = input("Your answer: ") # ответ пользователя
        if user_answer.lower() == "yes" and n%2 == 0:
            print("Correct!")
            i += 1
        elif user_answer.lower() == "no" and n%2 != 0:
            print("Correct!")
            i += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name)
            break
    else:
        print(f'Congratulations, {name}')

name = welcome_user()
game1(name)

if __name__ == "__main__":
    main()
