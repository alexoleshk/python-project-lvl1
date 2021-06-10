#!/usr/bin/env python3

from brain_games.common_funcs import greeting
from brain_games.games.calc import calc_game


def main():
    name = greeting()
    if calc_game(name):
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
