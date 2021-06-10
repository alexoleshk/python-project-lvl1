#!/usr/bin/env python3

from brain_games.common_funcs import greeting
from brain_games.games.gcd import gcd_game


def main():
    name = greeting()
    if gcd_game(name):
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
