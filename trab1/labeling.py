import cv2
import numpy as np
import copy
from collections import deque

lista = deque()
numero = 0
com_furo = 0

def criaLista(pixel,valor):
    global lista, numero, im_2
    if im_2[pixel[0], pixel[1]] == numero:
        return

    for x in range(-1, 2):
        for y in range(-1, 2):
            try:
                if im_2[pixel[0] + x, pixel[1] + y] == valor and not [pixel[0] + x, pixel[1] + y] in lista:
                    lista.append([pixel[0] + x, pixel[1] + y])
                    criaLista([pixel[0]+x,pixel[1]+y], valor)
            except:
                pass

def floodfill(pixel, valor):
    global lista, numero, im_2
    # if im_2[pixel[0],pixel[1]] == numero:
    #     return
    #
    # im_2[pixel[0],pixel[1]] = numero
    # for x in range(-1,2):
    #     for y in range(-1,2):
    #         try:
    #             if im_2[pixel[0]+x, pixel[1]+y] == valor:
    #                 # floodfill([pixel[0]+x,pixel[1]+y], valor)
    #                 lista.append([pixel[0]+x, pixel[1]+y])
    #         except:
    #             pass
    criaLista(pixel,valor)
    while len(lista) != 0:
        [x,y] = lista.pop()
        im_2[x,y] = numero



image = cv2.imread("bolhas.png",0)
cv2.namedWindow("image")
cv2.imshow("image", image)

cv2.waitKey(0)
height, width = image.shape
im_2 = copy.copy(image)

for x in range(width):
    if im_2[0,x] == 255:
        floodfill([0,x],255)
    if im_2[height-1, x] == 255:
        floodfill([height-1,x],255)

for y in range(width):
    if im_2[y,0] == 255:
        floodfill([y,0],255)
    if im_2[y, width-1] == 255:
        floodfill([y, width-1],255)

numero += 1
for x in range(width):
    for y in range(height):
        if im_2[x,y] == 255:
            floodfill([x,y],255)
            numero += 1

print(numero-1)

im_3 = copy.copy(im_2)

numero = 255
floodfill([0,0],0)
# for y in range(height):
#     for x in range(width):
#         if im_2[x,y] == 0:
#             floodfill([x,y],0)
#             if im_2[x-1,y] != 255:
#                 com_furo += 1
#                 floodfill([x-1,y],im_2[x-1,y])

cv2.imshow("image", im_2)

cv2.waitKey(0)
