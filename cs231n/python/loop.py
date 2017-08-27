animals = ['cat', 'dog', 'monkey']

for animal in animals:
  print(animal)
  
for idx, animal in enumerate(animals):
  print('#%d: %s' % (idx + 1, animal))
  
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
  legs = d[animal]
  print('A %s has %d legs' % (animal, legs))
  
for animal, legs in d.items():
  print('A %s has %d legs' % (animal, legs))