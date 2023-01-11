from homework.lesson01 import *
from homework.lesson02 import *

def main():
  # variables - a way to define something that you can update later
  #cake = 'Chocolate'

  # print('*1',cake)

  cake = 'Butter Cream'

  # print('*2',cake)
  
  # print(f'Lucie likes {cake} cake') # This way allows us to type a little more naturally
  # print("Lucie likes", cake, "cake")
  
  # The ' ' around chocolate means it is a string

  age = 10 # numbers dont need ' ' 
  # print(f'Lucie likes {cake} cake and she is {age}')
  
  # Booleans - True or False
  
  python = True
  
  # print(f'Lucie likes {cake} cake and she is {age}. Is she learning Python - {python}')

  # List Tuple Dictionary
  aList = [1,2,3,4] # is updatable (or mutable)
  aTuple = (1,2,3,4) # is not updatable (or immutable)
  
  aList.append(5)
  
  # Key / Value pair
  aDict = {
      "anteater": "A animal",
      "elephant": "Big Gray Animal"
  }
  # print('*3',aDict)
  # print('*4', aDict['anteater'])
  # print('*5', aDict['elephant'])

  animals = [
      {"anteater": "A animal"},
      {"elephant": "Big Gray Animal"}
  ]
  # print(animals[0]['anteater'])
  # print(animals[1]['elephant'])
  
  ADucktionary = {'Duck' : 'A fluffy animal'}, {'jygrehugij' : 'A bunch of letters'}
  print(ADucktionary[0])
  print(ADucktionary[0]['Duck'])
  print(ADucktionary[0])

  house = [
    {'room1': [{'circle': 'circle'},{'percent': 'percent'}]},
    {'room2': [{'perenthisis': 'perenthisis'},{'comma': 'comma'}]},
    {'room3': [{'square': 'square'},{'triangle': 'triangle'}]},
    {'room4': [{'period': 'period'},{'rectangle': 'rectangle'}]},
    {'room5': [{'heart': 'heart'}]},
    {'room6': [{'exclamation point': 'exclamation point'}]},
    {'room7': [{'question mark': 'question mark'}]},
  ]
  # Print the contents of the whole house
  print(house)
  
  # Print the contents of room 6
  print(house[5])
  
  # Print the triangle
  print(house[2]['room3'][1]['triangle'])


def lessons():
  lesson01()


if __name__ == "__main__":
    # main()
  lessons()