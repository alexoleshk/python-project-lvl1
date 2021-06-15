from brain_games.games.even import get_quest_ans_even


def get_task(game):
    tasks = {
        'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    }
    return tasks[game]


def get_question_answer(game):
    funcs = {
        'even': get_quest_ans_even
    }
    return funcs[game]()
