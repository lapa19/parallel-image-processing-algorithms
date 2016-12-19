import numpy as np
from numpy import array
from scipy import misc
from PIL import Image
import pymp
import datetime

a = datetime.datetime.now()
pymp.config.nested = True
face = misc.imread('my.pgm')
print (face.shape)
convx = array([[1/16, 2/16, 1/16],
	  [2/16, 4/16, 2/16],
	  [1/16, 2/16, 1/16]])
l=face.shape[0]
b=face.shape[1]
#padded = np.zeros((l+2,b+2))
padded = pymp.shared.array((l+2,b+2), dtype='uint8')
i=None
j=None
with pymp.Parallel(2) as p1:
	with pymp.Parallel(2) as p2: 
		for i in p1.range(0,l):
			for j in p2.range(0,b):
				padded[i+1][j+1]=face[i][j]


res = pymp.shared.array((l,b), dtype='uint8')
i=None
j=None
with pymp.Parallel(2) as p1:
	with pymp.Parallel(2) as p2: 
		for i in p1.range(1,l+1):
			for j in p2.range(1,b+1):
				res[i-1][j-1] = (convx[0][0]*padded[i-1][j-1] + convx[0][1]*padded[i-1][j]+convx[0][2]*padded[i-1][j+1]+ 
						convx[1][0]*padded[i][j-1]+convx[1][1]*padded[i][j] + convx[1][2]*padded[i][j+1]+ 
						convx[2][0]*padded[i+1][j-1]+ convx[2][1]*padded[i+1][j] +convx[2][2]*padded[i+1][j+1])
				
		
img = Image.fromarray(res)
img.save('my.png')
img.show()
b = datetime.datetime.now()
print(b-a)
