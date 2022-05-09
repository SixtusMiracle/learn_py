# sorted(a) - sort a set
# a - b members in set a that are not in b
# a | b members in set a or b
# a ^ b members in a or b but not both
# a & b members that are in both

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a | b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
