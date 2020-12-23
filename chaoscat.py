# Package needed
import numpy as np
from PIL import Image # or cv2
import imageio
import os


# Read original image
image = Image.open('cat.jpg')


# Check image size
# Because the image size need to be represented as N x N matrix, so we needed to reshape the image to N x N
print(np.array(image).shape)

# If your original pic is already square size, you could skip the below procedure
def make_square(image):
    x, y = image.size
    size = max(x, y)
    new_image = Image.new('RGBA', (size, size))
    new_image.paste(image, (int((size - x) / 2), int((size - y) / 2)))
    return new_image


image = make_square(image)


# Check image size is squared
print(np.array(image).shape)


# Save image for mapping
image = image.save('catmap.png') 


# Creating mapping images
image = np.array(Image.open("catmap.png"))
N = image.shape[0]
x,y = np.meshgrid(range(N), range(N))

x_map = (2*x+y) % N
y_map = (x+y) % N

for i in range(N+1):
    output_images = Image.fromarray(image)
    output_images.save("catmap_%03d.png" % i)
    image = image[x_map, y_map]


# Convert images to GIF
images = []
filenames = sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))

for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('catmap.gif', images, duration = 0.05)  # duration = interval time