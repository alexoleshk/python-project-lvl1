import random
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    counter = 2
    while counter <= int(sqrt(n)):
        if not n % counter:
            return False
        counter += 1
    return True


def get_quest_ans_prime():
    max_num = 20
    n = random.randint(1, max_num)
    question = 'Question: {}'.format(n)
    correct_answer = 'yes' if is_prime(n) else 'no'
    return question, correct_answer
