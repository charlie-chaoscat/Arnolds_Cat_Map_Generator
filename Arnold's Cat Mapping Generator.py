#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Package needed
import numpy as np
from PIL import Image # or cv2
import imageio
import os


# In[ ]:


# Read original image
image = Image.open('cat.jpg')


# In[ ]:


# Check image size
# Because the image size need to be represented as N x N matrix, so we needed to reshape the image to N x N
np.array(image).shape


# In[ ]:


# If your original pic is already square size, you could skip the below procedure
def make_square(image, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = image.size
    size = max(min_size, x, y)
    new_image = Image.new('RGBA', (size, size), fill_color)
    new_image.paste(image, (int((size - x) / 2), int((size - y) / 2)))
    return new_image


# In[ ]:


image = make_square(image)


# In[ ]:


# Check image size is squared
np.array(image).shape 


# In[ ]:


# Save image for mapping
image = image.save('Catmap.png') 


# In[ ]:


# Creating mapping images
image = np.array(Image.open("Catmap.png"))
N = image.shape[0]
x,y = np.meshgrid(range(N), range(N))

x_m = (2*x+y) % N
y_m = (x+y) % N

for i in range(N+1):
    output_images = Image.fromarray(image)
    output_images.save("catmap_%03d.png" % i)
    image = image[x_m,y_m]


# In[ ]:


# Convert images to GIF
images = []
filenames = sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))

for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('Catmap.gif', images, duration = 0.5)  # duration = interval time

