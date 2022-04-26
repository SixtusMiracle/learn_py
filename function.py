def main():
    # All functions return a value
    # if there's no return statement it returns None
    x = kitten()
    print(f'{x} is returned')

def kitten():
    print('Meow!')
    return 1

if __name__ == '__main__': main()
