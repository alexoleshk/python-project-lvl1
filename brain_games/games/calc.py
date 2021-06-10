import prompt
import random
import operator


def calc_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))

    print('What is the result of the expression?')
    attempts = 3
    for i in range(attempts):
        max_num = 99
        a = random.randint(1, max_num)
        b = random.randint(1, max_num)
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        op = random.choice(list(ops.keys()))
        print('Question: {} {} {}'.format(a, op, b))
        answer = prompt.integer('Your answer: ')
        right_answer = ops[op](a, b)
        if answer != right_answer:
            print("'{}' is wrong answer ;(."
                  " Correct answer was '{}'.".format(answer, right_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print('Congratulations, {}!'.format(name))
