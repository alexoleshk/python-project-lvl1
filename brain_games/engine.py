import prompt

ROUND = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    print(game.TASK)
    for _ in range(ROUND):
        question, correct_answer = game.get_question_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer "
                  "was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print('Congratulations, {}!'.format(name))
