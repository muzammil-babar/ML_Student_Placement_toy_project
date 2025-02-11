# -*- coding: utf-8 -*-
"""Machine Learning Toy Project.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19hNPbu3C8Vd6hiFGPhzF4Q7z6fOQUGNL
"""

import numpy as np
import pandas as pd

df = pd.read_csv('/content/placement.csv')

df = df.iloc[:,1:]
df.head()

"""'''
STEPS:
1. Preprocess + EDA + Feature Selection
2. Extract input and output cols
3. Scale the values
4. Train text split
5. Train the model
6. Evaluate the model/model selection
7. Deploy the model
'''
"""

import matplotlib.pyplot as plt

plt.scatter(df['cgpa'], df['iq'],c=df['placement'])

# Classifying through Logistic Regression
x = df.iloc[:,0:2]
y = df.iloc[:,-1]

x.shape

y.shape

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1) # we are telling that 10% of the data should go towards training.

x_train

y_train

x_test

y_test

from sklearn.preprocessing import StandardScaler

#  We are now going to scale the data.

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

x_train

x_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# model training
clf.fit(x_train, y_train)

# evaluation
y_pred = clf.predict(x_test)
y_pred

y_test

from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_pred)

from mlxtend.plotting import plot_decision_regions

plot_decision_regions(x_train, y_train.values, clf=clf, legend=2)

import pickle

pickle.dump(clf, open('model.pkl', 'wb'))

