import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model import SGDRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
#data = load_boston()

df = pd.read_csv('cara.csv', sep=';')
#print df 
#df = pd.read_cdfsv('caracteristicas_images.csv', sep=' ')

     
X = df[list(df.columns)[1:]]
mat = X.as_matrix()
##X.pop(0);
print mat
y = df['A58']



X_train, X_test, y_train, y_test = train_test_split(X, y)
X_scaler = StandardScaler()
y_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
y_train = y_scaler.fit_transform(y_train)
X_test = X_scaler.transform(X_test)
y_test = y_scaler.transform(y_test)
regressor = SGDRegressor(loss='squared_loss')
scores = cross_val_score(regressor, X_train, y_train, cv=5)
print 'Cross validation r-sqaured scores:', scores
print 'Average cross validation r-squared score:', np.mean(scores)
regressor.fit_transform(X_train, y_train)
print 'Test set r-squared score', regressor.score(X_test, y_test)

