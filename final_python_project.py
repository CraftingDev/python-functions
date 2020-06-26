#!/usr/bin/env python3
import PIL
# path = "C:/Users/User/Desktop"
from PIL import Image

im = Image("test.jpg")
new_im = im.rotate(90)
new_im = new_im.resize((640, 480))
new_im.save("test_new.jpg")
