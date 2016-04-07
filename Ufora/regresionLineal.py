import pyfora
import pandas as pd
from pyfora.pandas_util import read_csv_from_string
from pyfora.algorithms import linearRegression

print "Connecting..."
executor = pyfora.connect('http://localhost:30000')
print "Importing data..."
#raw_data = executor.importS3Dataset('ufora-test-data',
 #                                 'iid-normal-floats-20GB-20-columns.csv').result()

print "Parsing and regressing..."

#df = pd.read_csv('cara.csv', sep=';')
#print df 
#df = pd.read_cdfsv('caracteristicas_images.csv', sep=' ')

     
#X = df[list(df.columns)[1:]]
#mat = X.as_matrix()
##X.pop(0);
#print mat
#y = df['A58']
data_frame = pd.read_csv('cara.csv',sep=';')#
with executor.remotely:
    #data_frame = pd.read_csv('cara.csv',sep=';')#read_csv_from_string(raw_data)
    predictors = data_frame.iloc[:, :-1]
    responses = data_frame.iloc[:, -1:]

    regression_result = linearRegression(predictors, responses)
    coefficients = regression_result[:-1]
    intercept = regression_result[-1]


print 'coefficients:', coefficients.toLocal().result()
print 'intercept:', intercept.toLocal().result()
