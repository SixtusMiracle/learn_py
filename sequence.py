# game.index('Paper') - search through a list, returns the index
# game.print(game[1:5:2]) - slice of a list, works like range
# game.append('Computer') - add an item at the end of a list
# game.insert(0, 'Music') - add an item at a particular index
# game.remove('Paper') - remove an item
# game.pop(3) - returns the removed item
# del game[3] - removes an item by index or by slice
# print(', '.join(game)) - join to a list using string function join()
# print(len(game)) - length of a list

def main():
  game = [ 'Rock', 'Paper', 'Scissors','Lizard', 'Spock' ]
  print(len(game))
  print_list(game)

def print_list(o):
  for i in o: print(i, end = ' ', flush = True)
  print()

if __name__ == '__main__': main()