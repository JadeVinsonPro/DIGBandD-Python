# importing module
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
# dataset
data = pd.read_csv("Market_Basket_Optimisation.csv")

# printing the shape of the dataset
print(data.shape)

# printing the heading
data.head()

# Top 10 items
# importing module
import numpy as np

# Gather All Items of Each Transaction into Numpy Array
transaction = []
for i in range(0, data.shape[0]):
    for j in range(0, data.shape[1]):
        transaction.append(data.values[i, j])

# converting to numpy array
transaction = np.array(transaction)

print(transaction)
#  Transform Them a Pandas DataFrame
df = pd.DataFrame(transaction, columns=["items"])

# Put 1 to Each Item For Making Countable Table, to be able to perform Group By
df["incident_count"] = 1
print(df)
#  Delete NaN Items from Dataset
indexNames = df[df['items'] == "nan"].index
df.drop(indexNames, inplace=True)

# Making a New Appropriate Pandas DataFrame for Visualizations
df_table = df.groupby("items").sum().sort_values("incident_count", ascending=False).reset_index()

#  Initial Visualizations
style = df_table.head(10).style.background_gradient(cmap='Greens')

print(df_table.show())
print(df_table)
# Plotting treemap
# importing required module
import plotly.express as px

# to have a same origin
df_table["all"] = "all"

# creating tree map using plotly
fig = px.treemap(df_table.head(30), path=['all', "items"], values='incident_count',
                 color=df_table["incident_count"].head(30), hover_data=['items'],
                 color_continuous_scale='Greens',
                 )
# ploting the treemap

plt.show()
plt.savefig('graph.png')

# importing the required module
from mlxtend.preprocessing import TransactionEncoder

# initializing the transactionEncoder
te = TransactionEncoder()
te_ary = te.fit(transaction).transform(transaction)
dataset = pd.DataFrame(te_ary, columns=te.columns_)

# dataset after encoded
print(dataset)