
import cv2
from cv2 import imread
import matplotlib.pyplot as plt

im = cv2.imread("forza.png")

x = cv2.GaussianBlur(im,(5,5),cv2.BORDER_DEFAULT)

plt.imshow(x)

plt.show()