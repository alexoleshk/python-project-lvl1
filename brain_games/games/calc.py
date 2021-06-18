import random
import operator
TASK = 'What is the result of the expression?'
MAX_NUM = 25


def calculate_result(a, b, op, ops):
    return ops[op](a, b)


def get_question_answer():
    a = random.randint(1, MAX_NUM)
    b = random.randint(1, MAX_NUM)
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    op = random.choice(list(ops.keys()))
    question = 'Question: {} {} {}'.format(a, op, b)
    result = calculate_result(a, b, op, ops)
    correct_answer = str(result)
    return question, correct_answer
