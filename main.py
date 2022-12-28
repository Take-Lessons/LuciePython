# variables - a way to define something that you can update later
cake = 'Chocolate'

print('*1',cake)

cake = 'Butter Cream'

print('*2',cake)

print(f'Lucie likes {cake} cake') # This way allows us to type a little more naturally
print("Lucie likes", cake, "cake")

# The ' ' around chocolate means it is a string

age = 10 # numbers dont need ' ' 
print(f'Lucie likes {cake} cake and she is {age}')

# Booleans - True or False

python = True

print(f'Lucie likes {cake} cake and she is {age}. Is she learning Python - {python}')

# List Tuple Dictionary
aList = [1,2,3,4] # is updatable (or mutable)
aTuple = (1,2,3,4) # is not updatable (or immutable)

aList.append(5)

# Key / Value pair
aDict = {
    "anteater": "A animal",
    "elephant": "Big Gray Animal"
}
print('*3',aDict)
print('*4', aDict['anteater'])
print('*5', aDict['elephant'])

animals = [
    {"anteater": "A animal"},
    {"elephant": "Big Gray Animal"}
]
print(animals[0]['anteater'])
print(animals[1]['elephant'])