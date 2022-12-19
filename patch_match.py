import numpy as np
from skimage.io import imread,imshow
from matplotlib import pyplot as plt
from PIL import Image

def patch_match(source, target, patch_size):
    # Compute the dimensions of the source and target images
    source_height, source_width = source.shape[:2]
    target_height, target_width = target.shape[:2]
    
    # Initialize the nearest neighbor field with random offsets
    nnf = np.random.randint(0, target_height, size=(source_height, source_width, 2))
    
    # Iterate over the patches in the source image
    for i in range(0, source_height - patch_size + 1, patch_size):
        for j in range(0, source_width - patch_size + 1, patch_size):
            # Extract the patch from the source image
            source_patch = source[i:i+patch_size, j:j+patch_size]
            
            # Find the best matching patch in the target image
            best_match_dist = float('inf')
            best_match_coords = (0, 0)
            for ii in range(0, target_height - patch_size + 1, patch_size):
                for jj in range(0, target_width - patch_size + 1, patch_size):
                    # Extract the patch from the target image
                    target_patch = target[ii:ii+patch_size, jj:jj+patch_size]
                    
                    # Compute the distance between the two patches
                    patch_dist = np.sum((source_patch - target_patch) ** 2)
                    
                    # Update the best match if necessary
                    if patch_dist < best_match_dist:
                        best_match_dist = patch_dist
                        best_match_coords = (ii, jj)
            
            # Update the nearest neighbor field with the new best match
            nnf[i:i+patch_size, j:j+patch_size] = best_match_coords
    
    return nnf

"""
# Test the patch match function with a pair of test images
source = np.random.randint(0, 256, size=(256, 512, 3), dtype=np.uint8)
target = np.random.randint(0, 256, size=(256, 512, 3), dtype=np.uint8)
nnf = patch_match(source, target, patch_size=8)

print(nnf.shape)  # Output: (256, 512, 2)
"""

def synthesize_image(source, target, nnf, x1, y1, x2, y2):
    # Compute the dimensions of the source and target images
    source_height, source_width = source.shape[:2]
    target_height, target_width = target.shape[:2]
    
    # Initialize the synthesized image with the same shape as the source image
    synthesized = np.copy(source)
    
    # Iterate over the patches in the desired portion of the source image
    for i in range(y1, y2):
        for j in range(x1, x2):
            # Look up the best matching patch in the target image using the nearest neighbor field
            ii, jj = nnf[i, j]
            
            # Copy the best matching patch from the target image to the synthesized image
            synthesized[i, j] = target[ii, jj]
    print("Here, the type is",type(synthesized))
    return (synthesized/255)


def show_my_image(image):
    plt.imshow(image,cmap='gray')
    plt.show()

def show_my_image_to_float(image):
    # Convert the image data to float and scale it to the range [0, 1]
    image = image.astype(np.float32)
    
    # Display the image using the "gray" color map
    plt.imshow(image, cmap='gray')
    plt.show()

# Test the synthesize_image function with a pair of test images and a nearest neighbor field
source = imread('copy.jpg');print("Voici mon dtype : ",source.dtype)#;show_my_image(source)
height = source.shape[0]
weight = source.shape[1]

#target = np.random.randint(0, 255, size=(height, weight, 1), dtype=np.uint8);show_my_image(target)
target = imread("oops.jpg", as_gray=True)#;show_my_image(target) #To force the grey dimension


nnf = patch_match(source, target, patch_size=30) #Nearest neighbor field
"""synthesized = synthesize_image(source, target, nnf);show_my_image(synthesized)
plt.imsave('synthesized.jpg',synthesized)
print(synthesized.shape)  # Output: (256, 512, 3)"""

# Select a portion of the source and target images
source_portion = source[150:350, 350:550]#; show_my_image(source_portion)
target_portion = target[150:350, 350:550]#; show_my_image(target_portion)

synthesized_portion = synthesize_image(source, target, nnf, 100, 100, 200, 200);print("Here, the type is",type(synthesized_portion))
show_my_image(synthesized_portion)