import random
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUM = 100


def get_question_answer():
    n = random.randint(1, MAX_NUM)
    question = 'Question: {}'.format(n)
    correct_answer = 'no' if n % 2 else 'yes'
    return question, correct_answer
