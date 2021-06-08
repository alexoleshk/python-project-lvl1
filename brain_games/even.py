import prompt
import random

def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))

    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts = 3
    for i in range (attempts):
        max_num = 100
        n = random.randint(1, max_num)
        print('Question: {}'.format(n))
        answer = prompt.string('Your answer: ')
        right_answer = 'no' if n % 2 else 'yes'
        if answer != right_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, right_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print('Congratulations, {}!'.format(name))


