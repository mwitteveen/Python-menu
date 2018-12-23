from PIL import  Image
import os

im = Image.open((str(os.getcwd()) + "\\About info\\Logo.png"))
print (im.mode)
im.convert("RGBA").save((str(os.getcwd()) + "\\About info\\Logo.png"))