def main():
    soundsList = ('meow', 'meeeh', 'mooh')
    kitten(*soundsList)

def kitten(*args):
    if len(args):
        for sound in args:
            print(sound)
    else: print('Meow!')

if __name__ == '__main__': main()
