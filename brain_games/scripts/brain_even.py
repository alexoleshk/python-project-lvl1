#!/usr/bin/env python3

from brain_games.games.even import even_game
from brain_games.common_funcs import greeting


def main():
    name = greeting()
    if even_game(name):
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
