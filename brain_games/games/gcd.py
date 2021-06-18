import random
from math import gcd
TASK = 'Find the greatest common divisor of given numbers.'
MAX_NUM = 99


def get_question_answer():
    a = random.randint(1, MAX_NUM)
    b = random.randint(1, MAX_NUM)
    question = 'Question: {} {}'.format(a, b)
    correct_answer = str(gcd(a, b))
    return question, correct_answer
