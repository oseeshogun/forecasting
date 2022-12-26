import numpy as npzo
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('csv_temperatures.csv')

df['y'] = df['Temperature'].shift(-1)

print(df)

train = df[2800]
test = df[2800:]

test = test.drop(test.tail(1).index)

test = test.copy()
test['baseline_pred'] = test['Temperature']
