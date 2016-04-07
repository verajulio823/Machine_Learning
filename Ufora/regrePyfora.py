import pyfora
from pyfora.pandas_util import read_csv_from_string
from pyfora.algorithms import linearRegression

print "Connecting..."
executor = pyfora.connect('http://localhost:30000')
print "Importing data..."
raw_data = executor.importS3Dataset('ufora-test-data',
                                  'iid-normal-floats-20GB-20-columns.csv').result()

print "Parsing and regressing..."
with executor.remotely:
    data_frame = read_csv_from_string(raw_data)
    predictors = data_frame.iloc[:, :-1]
    responses = data_frame.iloc[:, -1:]

    regression_result = linearRegression(predictors, responses)
    coefficients = regression_result[:-1]
    intercept = regression_result[-1]


print 'coefficients:', coefficients.toLocal().result()
print 'intercept:', intercept.toLocal().result()
