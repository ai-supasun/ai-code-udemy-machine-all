# importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv',header = None)

transactions = []
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# training aprioi on the dataset
from apyori import apriori
# from efficient_apriori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)
# visualising the results
results = list(rules)
print(results)

