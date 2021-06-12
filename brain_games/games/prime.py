import prompt
from brain_games.common_funcs import check_answer


def prime_game(name):
    print('What number is missing in the progression?')
    attempts = 3
    for i in range(attempts):
        right_answer =
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if not check_answer(name, answer, right_answer):
            return False
    return True
