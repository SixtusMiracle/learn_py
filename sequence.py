# animals.items() - set of key value pairs
# animals.keys() - set of just the keys
# animals.values() - set of just the values
# print('lions' in animals) - search through, returns True or False
# animals.get('godzilla') - when you are not sure the key exists, if not found returns None

def main():
  animals_one = dict(kitten = 'meow', puppy = 'ruff', lion = 'grr') # using dictionary constructor
  animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
      'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
  print('found!' if 'lion' in animals else 'not found!')
  # print_dict(animals_one)

def print_dict(o):
    for k,v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()
