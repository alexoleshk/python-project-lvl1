from brain_games.games.even import get_quest_ans_even
from brain_games.games.progression import get_quest_ans_progr


def get_task(game):
    tasks = {
        'even': 'Answer "yes" if the number is even, otherwise answer "no".',
        'progression': 'What number is missing in the progression?',
    }
    return tasks[game]


def get_question_answer(game):
    funcs = {
        'even': get_quest_ans_even,
        'progression': get_quest_ans_progr,
    }
    return funcs[game]()
