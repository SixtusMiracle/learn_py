#!/usr/bin/python3

import random

def main():
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

if __name__ == '__main__': main()
