import random
from math import sqrt
import prompt
from brain_games.common_funcs import check_answer


def is_prime(n):
    if n < 2:
        return False
    counter = 2
    while counter <= int(sqrt(n)):
        if not n % counter:
            return False
        counter += 1
    return True


def prime_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    max_num = 20
    attempts = 3
    for i in range(attempts):
        n = random.randint(1, max_num)
        right_answer = 'yes' if is_prime(n) else 'no'
        print('Question: {}'.format(n))
        answer = prompt.string('Your answer: ')
        if not check_answer(name, answer, right_answer):
            return False
    return True


def get_quest_ans_prime():
    max_num = 20
    n = random.randint(1, max_num)
    question = 'Question: {}'.format(n)
    correct_answer = 'yes' if is_prime(n) else 'no'
    return question, correct_answer
