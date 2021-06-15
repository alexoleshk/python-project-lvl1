import random
from math import gcd


def get_quest_ans_gcd():
    max_num = 99
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    question = 'Question: {} {}'.format(a, b)
    correct_answer = gcd(a, b)
    return question, correct_answer
