from brain_games.games.calc import get_quest_ans_calc
from brain_games.games.even import get_quest_ans_even
from brain_games.games.gcd import get_quest_ans_gcd
from brain_games.games.progression import get_quest_ans_progr


def get_task(game):
    tasks = {
        'even': 'Answer "yes" if the number is even, otherwise answer "no".',
        'progression': 'What number is missing in the progression?',
        'calc': 'What is the result of the expression?',
        'gcd': 'Find the greatest common divisor of given numbers.',
    }
    return tasks[game]


def get_question_answer(game):
    funcs = {
        'even': get_quest_ans_even,
        'progression': get_quest_ans_progr,
        'calc': get_quest_ans_calc,
        'gcd': get_quest_ans_gcd,
    }
    return funcs[game]()
