#dataset taken from kaggle 

# import libraries

# 1. to handle the data
import pandas as pd
import numpy as np

# 2. To Viusalize the data
import matplotlib.pyplot as plt
import seaborn as sns

#3.To split the data 
from sklearn.model_selection import train_test_split

import keras
from keras import layers
from keras.models import Sequential
from keras.layers import Dense

import tensorflow as tf

#to test the model 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score , recall_score , accuracy_score , f1_score

df = pd.read_csv('heart_disease_health_indicators_BRFSS2015.csv')



x = df.drop('HeartDiseaseorAttack', axis =1)
y = df['HeartDiseaseorAttack']

#splitting the data for training and testing the data 

x_train, x_test , y_train, y_test=train_test_split(x, y, random_state=42 , test_size=0.25, shuffle= True )

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# Define model

model = Sequential()
model.add(Dense(500, input_dim=21, activation= "relu"))
model.add(Dense(100, activation= "relu"))
model.add(Dense(1))
model.summary() #Print model Summary
model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["Accuracy"]  )
model.fit(x_train, y_train, epochs = 10)
predictions = model.predict(x_test)
# For binary classification, use a threshold of 0.5
predicted_classes = (predictions > 0.5).astype(int).flatten()
accuracy = accuracy_score(y_test,predicted_classes)
print('Accuracy: %f' % accuracy)
# precision tp / (tp + fp)
precision = precision_score(y_test,predicted_classes,average='weighted')
print('Precision: %f' % precision)
# recall: tp / (tp + fn)
recall = recall_score(y_test,predicted_classes,average='weighted')
print('Recall: %f' % recall)
# f1: 2 tp / (2 tp + fp + fn)
f1 = f1_score(y_test,predicted_classes,average='weighted')
print('F1 score: %f' % f1)

import joblib
joblib.dump(model, 'model.joblib')
predictions = final_model.predict(x_test)
predictions
final_model = joblib.load('model.joblib')
