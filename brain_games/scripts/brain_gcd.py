#!/usr/bin/env python3
from brain_games.games.gcd import get_quest_ans_gcd
from brain_games.engine import engine


def main():
    task = 'Find the greatest common divisor of given numbers.'
    engine(task, get_quest_ans_gcd)


if __name__ == '__main__':
    main()
