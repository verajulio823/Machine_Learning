import pandas as pd
from pyfora.algorithms import GradientBoostedClassifierBuilder

builder = GradientBoostedClassifierBuilder(1, 1, 1.0)
#x = pandas.DataFrame({'x0': [-1,0,1], 'x1': [0,1,1]})
#y = pandas.DataFrame({'y': [0,1,1]})
df = pd.read_csv('caras.csv',sep=';')
x = df[list(df.columns)[1:]]
y = df['A0'] 

print y
fitter = builder.iterativeFitter(x, y)



# compute scores vs number of boosts
numBoosts = 5
scores = []
for ix in xrange(numBoosts):
    fitter = fitter.next()
    scores = scores + [fitter.model.score(x, y)]
