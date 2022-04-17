x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]

print(type(x))
print(type(y))
print(type(x[1]))
print(id(x[0]))
print(id(y[0]))

print()
if x[0] is y[0]:
  print('Yeah!')
else:
  print('Nope!')

print()
if x is y:
  print('Yeah!')
else:
  print('Nope!')

print()
if isinstance(y, tuple):
  print('tuple')
elif isinstance(y, list):
  print('list')
else:
  print('Nope!')