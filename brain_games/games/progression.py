import random
TASK = 'What number is missing in the progression?'
PROGR_LEN = 10
MAX_FIRST_ELEM = 42
MAX_STEP = 9


def generate_progression():
    step = random.randint(1, MAX_STEP)
    first_elem = random.randint(1, MAX_FIRST_ELEM)
    return list(range(first_elem,
                      first_elem + step * (PROGR_LEN - 1) + 1, step))


def get_question_answer():
    progression = generate_progression()
    index_to_hide = random.randint(0, PROGR_LEN - 1)
    correct_answer = str(progression[index_to_hide])
    progression[index_to_hide] = '..'
    question = 'Question: {}'.format(' '.join(map(str, progression)))
    return question, correct_answer
