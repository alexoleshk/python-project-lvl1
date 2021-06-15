import random
import operator


def get_quest_ans_calc():
    max_num = 25
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    op = random.choice(list(ops.keys()))
    question = 'Question: {} {} {}'.format(a, op, b)
    correct_answer = ops[op](a, b)
    return question, correct_answer
