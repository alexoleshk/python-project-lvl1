#!/usr/bin/env python3
from brain_games.games.progression import get_quest_ans_progression
from brain_games.engine import engine


def main():
    task = 'What number is missing in the progression?'
    engine(task, get_quest_ans_progression)


if __name__ == '__main__':
    main()
