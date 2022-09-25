#!/usr/bin/python3

import sys

def main():
    try:
        x = 5/0
    except ValueError:
        print('I caught a ValueError')
    except:
        print(f'unknown error: {sys.exc_info()[1]}')
    else:
        print('good job')
        print(x)

if __name__ == '__main__': main()
