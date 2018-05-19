
# coding: utf-8

# In[5]:

import numpy as np
import textwrap
import cv2
import stepic
import binascii
from Crypto.Cipher import AES
from steganography.steganography import Steganography
from Tkinter import *
import cv2
import Tkinter, tkFileDialog


# In[6]:

root = Tkinter.Tk()
root.withdraw()

encoded_image_path = tkFileDialog.askopenfilename()
encoded_image_path
encoded_img = cv2.imread(encoded_image_path)
cv2.imshow('Encoded_Image',encoded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:

key = Steganography.decode(encoded_image_path)


# In[8]:

key


# In[ ]:



