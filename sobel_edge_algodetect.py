#!/usr/bin/python3

import image
import math
import sys

img = image.Image("/path/to/image")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for x in range(1, img.getWidth()-1):
    for y in range(1, img.getHeight()-1):

        # initialize Gx to 0 and Gy to 0 for every pixel
        Gx = 0
        Gy = 0

        # top left pixel
        p = img.getPixel(x-1, y-1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        # intensity ranges from 0 to 765 (255 * 3)
        intensity = r + g + b

        # accumulate the value into Gx, and Gy
        Gx += -intensity
        Gy += -intensity

        # remaining the left column
        p = img.getPixel(x-1, y)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += -2 * (r + g + b)

        p = img.getPixel(x-1, y+1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += -(r + g + b)
        Gy += (r + g + b)

        # middle pixels
        p = img.getPixel(x, y-1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gy += -2 * (r + g + b)

        p = img.getPixel(x, y+1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gy += 2 * (r + g + b)

        # right column

        p = img.getPixel(x+1, y-1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += (r + g + b)
        Gy += -(r + g + b)

        p = img.getPixel(x+1, y)
        r = p.getRed()
        g = p.getRed()
        b = p.getBlue()

        Gx += 2 * (r + g + b)

        p = img.getPixel(x+1, y+1)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        Gx += (r + g + b)
        Gy += (r + g + b)

        # calculate the lenght of the gradient (Pythago Theorem)
        length = math.sqrt((Gx * Gx) + (Gy * Gy))

        # normalise the length of gradient to the range 0 to 255
        length = length / 4328 * 255
        
        length = int(length)

        # draw the length in the edge image
        newpixel = image.Pixel(length, length, length)
        newimg.setPixel(x, y, newpixel)


newimg.draw(win)
win.exitonclick()