import numpy as np
from numpy import array
from scipy import misc
from PIL import Image
import pymp
import datetime


MAX_IMAGESIZE = 4000
MAX_BRIGHTNESS = 255
GRAYLEVEL   =    256
MAX_FILENAME  =  256
MAX_BUFFERSIZE = 256

face = misc.imread('img0001.pgm')
pymp.config.nested = True
image1=face
#image2=face
print (face.shape)
y_size1=face.shape[0]
x_size1=face.shape[1]
image2 = pymp.shared.array((y_size1,x_size1), dtype='uint8')
hist=[0]*256
prob=[0.0]*256
myu=[0.0]*256
omega=[0.0]*256
sigma=[0.0]*256

def otsu_th():
  print("Otsu's binarization process starts now.\n")
  #/* Histogram generation */
  for y in range(0,y_size1):
    for x in range(0,x_size1):
      hist[image1[y][x]] += 1

  #/* calculation of probability density */
  for i in range(0,GRAYLEVEL):
    prob[i] = float(hist[i]) / (x_size1 * y_size1)
  for i in range(0, 256):
      print("Serial: " + str(prob[i]))
  #/* omega & myu generation */
  omega[0] = prob[0]
  myu[0] = 0.0      #/* 0.0 times prob[0] equals zero */
  for i in range(1,GRAYLEVEL):
    omega[i] = omega[i-1] + prob[i]
    myu[i] = myu[i-1] + i*prob[i]

  '''/* sigma maximization
     sigma stands for inter-class variance
     and determines optimal threshold value */'''
  threshold = 0
  max_sigma = 0.0
  for i in range(0,GRAYLEVEL-1):
    if (omega[i] != 0.0 and omega[i] != 1.0):
      sigma[i] = ((myu[GRAYLEVEL-1]*omega[i] - myu[i])**2) / (omega[i]*(1.0 - omega[i]))
    else:
      sigma[i] = 0.0
    if (sigma[i] > max_sigma):
      max_sigma = sigma[i]
      threshold = i

  print("\nthreshold value = "+ str(threshold))

  #/* binarization output into image2 */
  x_size2 = x_size1
  y_size2 = y_size1

  with pymp.Parallel(2) as p1:
      with pymp.Parallel(2) as p2:
          for y in p1.range(0,y_size2):
            for x in p2.range(0,x_size2):
              if (image1[y][x] > threshold):
                        image2[y][x] = MAX_BRIGHTNESS
              else:
                        image2[y][x] = 0
  print("hi")

a = datetime.datetime.now()
otsu_th()
b = datetime.datetime.now()
print("Time: "+str(b-a))
img = Image.fromarray(image2)
img.save('my.pgm')
img.show()
