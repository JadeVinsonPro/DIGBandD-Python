import pandas as pd

dict_from_csv = {}
dict_from_csv = pd.read_csv('databaseTDB.csv', header=None, index_col=0, squeeze=True).to_dict()
print(dict_from_csv)