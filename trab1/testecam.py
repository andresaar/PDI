import cv2
import numpy as np
cam = cv2.VideoCapture()
cam.open(0)

while True:

    ret, image = cam.read()
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    image_eq = cv2.equalizeHist(image)

    image = np.hstack((image,image_eq))

    cv2.imshow("teste", image)

    key = cv2.waitKey(10)

    if key == 27:
        break

cv2.destroyAllWindows()
cam.release()