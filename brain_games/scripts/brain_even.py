#!/usr/bin/env python3
from brain_games.games.even import get_quest_ans_even
from brain_games.engine import engine


def main():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine(task, get_quest_ans_even)


if __name__ == '__main__':
    main()
