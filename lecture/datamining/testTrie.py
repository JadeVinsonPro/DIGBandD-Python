myList = [1,10,5,7,12]
valueToBeRemoved = [1,10]
myList = [value for value in myList
          if value != valueToBeRemoved]

print(myList)
