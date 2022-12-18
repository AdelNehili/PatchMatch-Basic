import numpy as np
from skimage.io import imread,imshow
from matplotlib import pyplot as plt


def patch_match(image, patch_size, n_iterations):
    # Initialize a random set of patches in the image
    patch_locations = np.random.randint(0, image.shape[0] - patch_size, size=(n_iterations, 2))
    for y,x in patch_locations:
        patches = image[y:y+patch_size,x:x+patch_size]

    # Iteratively update patch locations and find best-matching patches
    for iteration in range(n_iterations):
        for i, patch in enumerate(patches):
            # Find the patch in the image that best matches the current patch
            best_match = find_best_match(image, patch)
            # Update the patch location to the location of the best-matching patch
            patch_locations[i] = best_match

        # Update the patches based on the new patch locations
        patches = [image[x:x+patch_size, y:y+patch_size] for x, y in patch_locations]

    # Synthesize the completed image using the patches and patch locations
    completed_image = synthesize_image(image, patches, patch_locations)
    return completed_image

def find_best_match(image, patch):
    # Calculate the sum of squared differences between the patch and all other patches in the image
    ssd = np.sum((image - patch) ** 2, axis=(2, 3))
    # Find the location of the patch with the lowest SSD
    best_match = np.unravel_index(np.argmin(ssd), ssd.shape)
    return best_match

def synthesize_image(image, patches, patch_locations):
    # Create an empty image with the same shape as the input image
    completed_image = np.zeros_like(image)
    # Fill in the image with the patches at their corresponding locations
    for patch, (x, y) in zip(patches, patch_locations):
        completed_image[x:x+patch_size, y:y+patch_size] = patch
    return completed_image

image = imread('copy.png')
plt.figure()
imshow(image)

print("Voici la matrice de l'image : \n",image)
patch_size = 2
n_iterations = 5
#patch_match(image, patch_size, n_iterations)

patch_start_point = np.random.randint(0, image.shape[0] - patch_size, size=(n_iterations, 2))
print("Voici la patch_start_point : \n",patch_start_point,"\n")
for y,x in patch_start_point:
    #print("Je suis en position y=%d, x=%d et la valeur du pixel vaut %d \n"%(y,x,image[y,x]))
    patches = image[y:y+patch_size,x:x+patch_size]
print("Voici les patches : \n",patches)