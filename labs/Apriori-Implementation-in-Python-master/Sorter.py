import csv

myFile = open('databaseTDB.csv', 'w', newline = '')
with myFile:
    for line in open("databaseTDB.csv"):
        transaction = line.strip('\n')
        transaction = transaction.split(',') #returns a list ["1","50","60"]
        transaction.sort()
        print(transaction," ")
        writer = csv.writer(myFile)
        #writer.writerows(transaction)
        writer.writerow(transaction)
