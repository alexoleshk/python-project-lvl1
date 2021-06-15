import prompt
from brain_games.helpers import get_task, get_question_answer


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
            print("'{}' is wrong answer ;(. Correct answer "
                  "was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print('Congratulations, {}!'.format(name))
