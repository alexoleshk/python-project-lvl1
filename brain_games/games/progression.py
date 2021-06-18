import random
TASK = 'What number is missing in the progression?'
PROGR_LEN = 10


def get_question_answer():
    step = random.randint(1, 9)
    first_elem = random.randint(1, 42)
    progression = list(range(first_elem,
                             first_elem + step * (PROGR_LEN - 1) + 1, step))
    index_to_hide = random.randint(0, PROGR_LEN - 1)
    correct_answer = str(progression[index_to_hide])
    progression[index_to_hide] = '..'
    progr_str_with_hidden = ' '.join(map(str, progression))
    question = 'Question: {}'.format(progr_str_with_hidden)
    return question, correct_answer
