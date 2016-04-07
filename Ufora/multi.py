import pyfora

ufora = pyfora.connect('http://localhost:30000')



X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4


def multi(X,Y):
	r2 = []
	for i in range(len(X)):
		r = []
		for j in range(len(Y[0])):
			s = 0
			for k in range(len(Y)):
				s = s + X[i][k] * Y[k][j]
			r = r + [s]
		r2 = r2 + [r]
	#r2[0][0]=999
	return r2        

def test(A,B):
	C=A+B
	return C	

# iterate through rows of X
with ufora.remotely.downloadAll():
	A=[2,'asdas',2.0]
	result2 = test(A,A)
	result = multi(X,Y)	

print result2
for r in result:
   print(r)
