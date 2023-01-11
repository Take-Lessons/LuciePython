def lesson01():
  animals = ['Anteater', 'Elephant', 'Tiger', 'Bear']

  # Print the whole list
  print(animals)
  # Print just the Tiger (remember it starts at 0)
  print(animals[2])
  # Add Panther to the list and print the whole list
  animals.append('Panther')
  print(animals)
  
  zoo = [
    {
    "name": "Bronks Zoo",
    "Location": "NYC",
    }, 
    {
    "name": "Lucies Zoo",
    "Loation": "NJ"
    }
  ]
  
  # Print the whole list
  print(zoo)
  # Print the 1st Dictionary
  print(zoo[0])
  # Print Lucies Zoo
  print(zoo[1]["name"])
