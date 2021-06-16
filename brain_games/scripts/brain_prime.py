#!/usr/bin/env python3
from brain_games.games.prime import get_quest_ans_prime
from brain_games.engine import engine


def main():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine(task, get_quest_ans_prime)


if __name__ == '__main__':
    main()
