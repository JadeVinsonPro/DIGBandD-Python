#supprimer element d'une liste
myList = [1,10,5,7,12]
myList = list(filter((1).__ne__,myList))

print(myList)

#autre
myList = [1,10,5,7,12]
valuToBeRemoved = 1

myList = list(filter((1).__ne__,myList))
result = filter(lambda val: val != valuToBeRemoved,myList)

print(list(result))

myList = [1,10,5,7,12]
valueToBeRemoved = 1

myList = [value for value in myList if value != valueToBeRemoved]
print(myList)
