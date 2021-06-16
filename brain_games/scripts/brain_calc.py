#!/usr/bin/env python3
from brain_games.games.calc import get_quest_ans_calc
from brain_games.engine import engine


def main():
    task = 'What is the result of the expression?'
    engine(task, get_quest_ans_calc)


if __name__ == '__main__':
    main()
