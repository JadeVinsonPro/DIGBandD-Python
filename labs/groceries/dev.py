import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


grocery = pd.read_csv('GroceryStoreDataSet.csv', names = ['Products'], sep = ',')

#print(grocery.describe())

grocery_df = list(grocery["Products"].apply(lambda x:x.split(",") ))
#print(grocery_df)

te = TransactionEncoder()
te_data = te.fit(grocery_df).transform(grocery_df)
gdf = pd.DataFrame(te_data, columns = te.columns_)
gdf = gdf.replace(False,0)


gdf = gdf.replace(True,1)
print(gdf)

gdf.sum().to_frame('Frequency').sort_values('Frequency',ascending=False).plot(kind='bar',
                                                                                  figsize=(12,8),
                                                                                  title="Frequent Items")

plt.savefig('../groceries/graph.png')
print(plt.show())

gdf1 = apriori(gdf, min_support = 0.2, use_colnames = True, verbose = 1)

gdf1.sort_values(by = "support" , ascending = False)

gdf_rules = association_rules(gdf1, metric = 'confidence', min_threshold = 0.6)
gdfFin = gdf_rules.sort_values(by = "lift", ascending = False)

print(gdfFin)