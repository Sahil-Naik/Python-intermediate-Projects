# This program is used to convert text into hand written img.
# Enter a text and wait for few seconds for the program to process it.
# 'pywhatkit' is a python-based library, which helps to convert any text to handwritting and written a png format of that image.

import pywhatkit
u_text = input("Enter some text: ")
pywhatkit.text_to_handwriting(u_text, rgb=[0,0,255])
