import random
import operator

TASK = 'What is the result of the expression?'
MAX_NUM = 25


def calculate_result(a, b, op):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    return ops[op](a, b)


def get_question_answer():
    a = random.randint(1, MAX_NUM)
    b = random.randint(1, MAX_NUM)
    op = random.choice(['+', '-', '*'])
    question = 'Question: {} {} {}'.format(a, op, b)
    result = calculate_result(a, b, op)
    correct_answer = str(result)
    return question, correct_answer
