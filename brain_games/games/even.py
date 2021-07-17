import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUM = 100


def is_even(n):
    return n % 2 == 0


def get_question_answer():
    n = random.randint(1, MAX_NUM)
    question = 'Question: {}'.format(n)
    correct_answer = 'yes' if is_even(n) else 'no'
    return question, correct_answer
