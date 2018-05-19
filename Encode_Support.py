
# coding: utf-8

# In[1]:

import numpy as np
import textwrap
import cv2
import stepic
import binascii
from Crypto.Cipher import AES
from steganography.steganography import Steganography

def Blocks_16_Bit(plain_text):
    if(len(plain_text)==0):
        return "Invalid input"
    byte_concat = len(plain_text)%16
    plain_text_concat = plain_text + (16-byte_concat)*'0'
    return plain_text_concat
    
def Channel_select(path):
    img = cv2.imread(path)
    blue,green,red = cv2.split(img)
    chose_image = raw_input("Enter the image channel to encode the key (blue, red, green): ")
    channel_dict = {"red":red,"blue":blue,"green":green}
    path_split = path.split('.')
    selected_image = path_split[0]+chose_image+'.'+path_split[1]
    cv2.imwrite(selected_image,channel_dict[chose_image])
    
    return selected_image

def Encode_key(channel_path,key):
    path_split = channel_path.split('.')
    encoded_path = path_split[0]+'encoded.'+path_split[1]
    encoded_image = Steganography.encode(channel_path,encoded_path,key)
    return encoded_path

def Encode_image(src_img,key):
    original_image = cv2.imread(src_img)
    key_image = Channel_select(src_img)
    #remaining_channel_keys = channel_dict.keys()
    encoded_image = Encode_key(key_image,key)
    encoded_img = cv2.imread(encoded_image)
    cv2.imshow('Encoded Image',encoded_img)
    cv2.imshow('Original Image',original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def File_process(file_to_encrypt):
    file_data = Open_file(file_to_encrypt)
    concat_pt = Blocks_16_Bit(file_data)
    key = raw_input("Enter the key (must be 16 bytes): ")
    encryption_suite = AES.new(key)
    cipher_text = encryption_suite.encrypt(concat_pt)
    encoded_file = open('test_encoded.txt','w+')
    encoded_file.write(cipher_text)
    return key
    

def Open_file(path):
    data = open(path,'r')
    return data.read()


# In[ ]:



