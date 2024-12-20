# -*- coding: utf-8 -*-
"""Copy of Project 10.Heart Disease Pridiction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17cTi7Zt4GDBnb-YBHRKolf7Wl3Dorth8

importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Processing"""

# loading the csv data to a Pandas DataFrame
heart_data = pd.read_csv('/content/data.csv')

# print first 5 rows of dataset
heart_data.head()

# print the last 5 rows of dataset
heart_data.tail()

#number of rows and cols in dataset
heart_data.shape

# getting some info about the data
heart_data.info()

# checking for missing values
heart_data.isnull().sum()

# statistical measures about the data
heart_data.describe()

# checking the distribution of target variable
heart_data['target'].value_counts()

"""1 -->Defective heart
0 -->Healthy heart

Splitting the Features and Target
"""

X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

print(X)

print(Y)

"""Splitting the data int Training data and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training

Logistic Regression
"""

model = LogisticRegression()

# training the LogisticRegression model with Traing data
model.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Score
"""

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data:', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data:', test_data_accuracy)

"""Building a predictive system"""

input_data = (43,0,0,132,341,1,0,136,1,3,1,0,3)

# change the input data as numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The person does not have a heart disease')
else:
  print('The person have heart disease')

