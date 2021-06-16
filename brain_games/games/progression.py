import random


def get_quest_ans_progression():
    progr_len = 10
    step = random.randint(1, 9)
    first_elem = random.randint(1, 42)
    progression = list(range(first_elem,
                             first_elem + step * (progr_len - 1) + 1, step))
    index_to_hide = random.randint(0, progr_len - 1)
    correct_answer = progression[index_to_hide]
    progression[index_to_hide] = '..'
    progr_str_with_hidden = ' '.join(map(str, progression))
    question = 'Question: {}'.format(progr_str_with_hidden)
    return question, correct_answer
