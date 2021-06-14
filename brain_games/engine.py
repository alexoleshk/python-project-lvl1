import prompt
from brain_games.games.even import get_answers_even


def get_task(game):
    tasks = {
        'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    }
    return tasks[game]


def get_answers(game):
    funcs = {
        'even': get_answers_even
    }
    return funcs[game]()


def engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    print(get_task(game))
    attempts = 3
    for i in range(attempts):
        answer, correct_answer = get_answers(game)
        if answer != correct_answer:
            print("'{}' is wrong answer ;(."
                  " Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print('Congratulations, {}!'.format(name))
