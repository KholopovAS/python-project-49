import random

from brain_games.cli import welcome_user

print("brain-prime\n")
name = welcome_user()
print('Answer "yes" if the number is even, otherwise answer "no"')


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    correct_answers = 0
    for _ in range(3):
        num = random.randint(1, 100)
        user_answer = input(f'''Question: {num} 
Your answer:''')
        if (is_prime(num) and user_answer.lower() == 'yes') or \
                (not is_prime(num) and user_answer.lower() == 'no'):
            correct_answers += 1
            print("Correct!")
        else:
            print("is wrong answer ;(")
    if correct_answers >= 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
