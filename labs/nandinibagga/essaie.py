# importation des bibliothèques utilisées

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns

from mlxtend.frequent_patterns import association_rules, apriori

#lecture du fichier CSV
document = pd.read_csv("bread basket.csv")

#affichage des 5 premières transactions
#print(df.head())

#affichage des informations principales du fichier CSV
# (le nombre de lignes, le minimum, les quartiles et le maximum)

print("Le document traité comprend un total de transactions de :\n")
print(document.describe().loc[['count']])
print("\nLes informations ")
print(document.describe())

#affichage du nom des colonnes
print(document.info())



# importing module
import numpy as np

# Gather All Items of Each Transactions into Numpy Array
transaction = []
for i in range(0, document.shape[0]):
    for j in range(0, document.shape[1]):
        transaction.append(document.values[i,j])

# converting to numpy array
transaction = np.array(transaction)

#  Transform Them a Pandas DataFrame
df = pd.DataFrame(transaction, columns=["items"])

# Put 1 to Each Item For Making Countable Table, to be able to perform Group By
df["incident_count"] = 1

#  Delete NaN Items from Dataset
indexNames = df[df['items'] == "nan" ].index
df.drop(indexNames , inplace=True)

# Making a New Appropriate Pandas DataFrame for Visualizations
df_table = df.groupby("items").sum().sort_values("incident_count", ascending=False).reset_index()

#  Initial Visualizations

# importing the required module
from mlxtend.preprocessing import TransactionEncoder

# initializing the transactionEncoder
te = TransactionEncoder()
te_ary = te.fit(transaction).transform(transaction)
dataset = pd.DataFrame(te_ary, columns=te.columns_)

# dataset after encoded
print(dataset)
#print(df_table.head(10).style.background_gradient(cmap='Greens'))
# importing the required module
from mlxtend.frequent_patterns import apriori, association_rules


# Extracting the most frequest itemsets via Mlxtend.
# The length column has been added to increase ease of filtering.
frequent_itemsets = apriori(dataset, min_support=0.01, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

# printing the frequent itemset
print(frequent_itemsets)
