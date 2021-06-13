# Script to plot the THEMIS images with the crater boxes drawn on.
# Images are 416x416 .png files
# Labels are .txt files in the format:
#   <ID> <x> <y> <width> <height>

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from PIL import Image

imageFolder = "./THEMIS/data_images"
labelFolder = "./THEMIS/data_labels"

imagePath = imageFolder+"/aeolis_29_3.png"

## Create a Rectangle patch
#rect = patches.Rectangle((50, 100), 40, 30, linewidth=1, edgecolor='r', facecolor='none')

## Add the patch to the Axes
#ax.add_patch(rect)

plt.figure()
plt.imshow(mpimg.imread(imagePath), cmap='gray')
plt.draw()
plt.show()
