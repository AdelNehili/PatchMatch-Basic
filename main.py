from patch_match import patch_match
import numpy as np
from skimage.io import imread,imshow
from matplotlib import pyplot as plt

image = imread('copy.jpg')
#plt.imshow(image,cmap='gray')
plt.show()

print("Voici la matrice de l'image : \n",image.shape)
patch_size = 4
n_iterations = 5

patch_match(image, patch_size, n_iterations)