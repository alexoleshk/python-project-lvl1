import random
import operator

TASK = 'What is the result of the expression?'
MAX_NUM = 25
OPS = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def calculate(operand_one, operand_two, operation):
    return OPS[operation](operand_one, operand_two)


def get_question_answer():
    operand_two = random.randint(1, MAX_NUM)
    operand_one = random.randint(1, MAX_NUM)
    operation = random.choice(list(OPS.keys()))
    question = '{} {} {}'.format(operand_one, operation, operand_two)
    result = calculate(operand_one, operand_two, operation)
    correct_answer = str(result)
    return question, correct_answer
