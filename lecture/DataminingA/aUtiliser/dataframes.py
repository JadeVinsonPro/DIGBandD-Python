import pandas as pd

from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

dataset = pd.read_csv('databaseTDB.csv', header=None)
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
df
apriori(df, min_support=0.6)

frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
print(frequent_itemsets)