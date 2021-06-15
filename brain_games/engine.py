import prompt
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


def engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    print(get_task(game))
    rounds = 3
    for i in range(rounds):
        question, correct_answer = get_question_answer(game)
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != str(correct_answer):
            print("'{}' is wrong answer ;(."
                  " Correct answer was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print('Congratulations, {}!'.format(name))
