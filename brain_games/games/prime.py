import random
from math import sqrt
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUM = 20


def is_prime(n):
    if n < 2:
        return False
    counter = 2
    while counter <= int(sqrt(n)):
        if not n % counter:
            return False
        counter += 1
    return True


def get_question_answer():
    n = random.randint(1, MAX_NUM)
    question = 'Question: {}'.format(n)
    correct_answer = 'yes' if is_prime(n) else 'no'
    return question, correct_answer
