import random


def get_quest_ans_even():
    max_num = 100
    n = random.randint(1, max_num)
    question = 'Question: {}'.format(n)
    correct_answer = 'no' if n % 2 else 'yes'
    return question, correct_answer
