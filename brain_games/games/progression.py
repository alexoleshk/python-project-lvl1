import random
import prompt
from brain_games.common_funcs import check_answer


def progression_game(name):
    print('What number is missing in the progression?')
    progr_len = 10
    attempts = 3
    for i in range(attempts):
        step = random.randint(1, 9)
        first_elem = random.randint(1, 99)
        progression = list(range(first_elem,
                                 first_elem + step * (progr_len - 1) + 1, step))
        index_to_hide = random.randint(0, progr_len - 1)
        right_answer = progression[index_to_hide]
        progression[index_to_hide] = '..'
        question = ' '.join(map(str, progression))
        print('Question: {}'.format(question))
        answer = prompt.integer('Your answer: ')
        if not check_answer(name, answer, right_answer):
            return False
    return True


def get_quest_ans_progr():
    PROGR_LEN = 10
    # правильно ли тут писать PROGR_LEN заглавными?
    # может вообще вынести PROGR_LEN за пределы функции?
    step = random.randint(1, 9)
    first_elem = random.randint(1, 42)
    progression = list(range(first_elem,
                             first_elem + step * (PROGR_LEN - 1) + 1, step))
    index_to_hide = random.randint(0, PROGR_LEN - 1)
    correct_answer = progression[index_to_hide]
    progression[index_to_hide] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
