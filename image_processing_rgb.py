#!/usr/bin/python3

import image

img = image.Image("/Users/jpereira/Desktop/python.png")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()
        newpixel = image.Pixel(newred, newgreen, newblue)
        img.setPixel(col, row, newpixel)
    # img.draw(win)   

img.draw(win)
win.exitonclick()


