dict = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4}
delete = []
for k,v in dict.items():
    if v%2 == 1:
        delete.append(k)
for i in delete:
    del dict[i]


print(dict)