import random
import prompt
from brain_games.common_funcs import check_answer


def progression_game(name):
    print('')
    attempts = 3
    for i in range(attempts):
        print('Question: {} {}'.format(a, b))
        answer = prompt.integer('Your answer: ')
        right_answer =
        if not check_answer(name, answer, right_answer):
            return False
    return True
