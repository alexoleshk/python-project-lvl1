import random
import prompt
from math import gcd
from brain_games.common_funcs import check_answer


def gcd_game(name):
    print('Find the greatest common divisor of given numbers.')
    max_num = 99
    attempts = 3
    for i in range(attempts):
        a = random.randint(1, max_num)
        b = random.randint(1, max_num)
        print('Question: {} {}'.format(a, b))
        answer = prompt.integer('Your answer: ')
        right_answer = gcd(a, b)
        if not check_answer(name, answer, right_answer):
            return False
    return True
