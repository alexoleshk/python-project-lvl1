import random
import operator
import prompt
from brain_games.common_funcs import check_answer


def calc_game(name):
    print('What is the result of the expression?')
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    max_num = 99
    attempts = 3
    for i in range(attempts):
        a = random.randint(1, max_num)
        b = random.randint(1, max_num)
        op = random.choice(list(ops.keys()))
        print('Question: {} {} {}'.format(a, op, b))
        answer = prompt.integer('Your answer: ')
        right_answer = ops[op](a, b)
        if not check_answer(name, answer, right_answer):
            return False
    return True
