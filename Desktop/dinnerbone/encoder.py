from PIL import Image
#from __future__ import print_function as print
import os
combined = Image.open("plchldr.png")
db = Image.open("dinnerbone.png")
for i in range(1,428):
    box = (0,480*(i-1),2,480*i)
    region = db.crop(box)
    pbox = (2*(i-1),0,2*i,480)
    combined.paste(region, pbox)
combined.show()
