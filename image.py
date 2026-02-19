import numpy as np
from PIL import Image

a = Image.open('1000004993.jpg')
b= np.array(a)
c= np.shape(b)


flip_h =  120+b 
Image.fromarray(flip_h).save("flip_h.jpg")

flip =  flip_h[::-1]
Image.fromarray(flip).save("flip.jpg")


print(flip_h) 
   