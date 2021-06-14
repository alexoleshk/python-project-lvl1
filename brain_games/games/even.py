import prompt
import random
from brain_games.common_funcs import check_answer


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    max_num = 99
    attempts = 3
    for i in range(attempts):
        n = random.randint(1, max_num)
        print('Question: {}'.format(n))
        answer = prompt.string('Your answer: ')
        right_answer = 'no' if n % 2 else 'yes'
        if not check_answer(name, answer, right_answer):
            return False
    return True


def get_answers_even():
    max_num = 100
    n = random.randint(1, max_num)
    print('Question: {}'.format(n))
    answer = prompt.string('Your answer: ')
    correct_answer = 'no' if n % 2 else 'yes'
    return answer, correct_answer