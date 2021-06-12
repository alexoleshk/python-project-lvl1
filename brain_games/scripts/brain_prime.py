#!/usr/bin/env python3

from brain_games.common_funcs import greeting
from brain_games.games.prime import prime_game


def main():
    name = greeting()
    if prime_game(name):
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
