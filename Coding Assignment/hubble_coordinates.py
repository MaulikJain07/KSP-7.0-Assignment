import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/maulik/Documents/KSP-7.0-Assignment/Coding Assignment/hubble-lrg3757.bmp',cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray')
plt.title("Hover your mouse over the image to find coordinates!")
plt.show()