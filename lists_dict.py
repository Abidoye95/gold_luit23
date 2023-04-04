var = []

print(type(var))

var2 = [251, 30, 35]

print(var2)

numbers = range(0, 20)

print(list(numbers))

for number in numbers:
    print(number*2)
   
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
print(len(var2))

var2.append(400)
print(var2)



import random
r = random.randint(1, 101)
print(r)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.keys())
print(thisdict.values())


a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
a['doughnut'] = 'snack'
print(a['apple'])
