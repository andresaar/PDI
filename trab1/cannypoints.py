import cv2
import numpy as np
from random import *


step = 5
jitter = 3
raio = 3

image = cv2.imread("clara.jpeg")

height, width, depth = image.shape

xrange, yrange = np.arange(0,int(height/step)),np.arange(0,int(width/step))

for i in range(len(xrange)):
    xrange[i] = int(xrange[i]*step + step/2)
for j in range(len(yrange)):
    yrange[j] = int(yrange[j]*step + step/2)

points = np.ones([height,width, depth],dtype=np.uint8)*255

np.random.shuffle(xrange)

for i in xrange:
    np.random.shuffle(yrange)
    for j in yrange:
        x = i + randrange(-jitter,jitter)
        y = j + randrange(-jitter, jitter)
        pixel = image[x,y].tolist()
        cv2.circle(points,(y,x),raio,pixel,-1,cv2.LINE_AA)

cv2.imshow("pontilhada", np.hstack((image,points)))
cv2.imwrite("pontilhada.jpg", points)
cv2.waitKey(0)
cv2.destroyAllWindows()