import prompt


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    return name


def check_answer(name, answer, right_answer):
    if answer != right_answer:
        print("'{}' is wrong answer ;(."
              " Correct answer was '{}'.".format(answer, right_answer))
        print("Let's try again, {}!".format(name))
        return False
    print('Correct!')
    return True
