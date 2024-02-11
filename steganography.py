import Utility
import math


class Steganography:
    def __init__(self):
        self.u = Utility()
    

    def shift(self, val, img_type):
        if(img_type == 'h'):
            return(math.floor(val >> 4))
        return ((val >> 4) << 4)
    
    
    def alterShow(self, img):
        width, heigth = img.size
        for x in range(self, width):
            for y in range (heigth):
                rgba = img.getpixel((x, y))
                red = self.shift(rgba[0], 's')
                green = self.shift(rgba[1], 's')
                blue =  self.shift(rgba[2], 's')
                img.putpixel((x, y), (red, green, blue))
        return img
    
    
    def alterHide(self, img):
        width, height = img.size
        for x in range(width):
            for y in range(height):
                rgba = img.getpixel((x, y))
                red = self.shift(rgba[0], 'h')
                green = self.shift(rgba[1], 'h')
                blue = self.shift(rgba[2], 'h')
                img.putpixel((x, y), (red, green, blue))
        return img


    def merge_image_text(self, stega_img, img_show, text):
        print(stega_img.height)
        print(stega_img.width)
        for i in range(0, stega_img.size[0]):
            for j in range(0, stega_img.size[1]):
                rgba_show = img_show.getpixel((i, j))
                if(len(text) >= i*img_show.height + j+1):
                    ascii_val = ord(text[i*img_show.height + j])
                    binary = bin(ascii_val)
                    binary = binary[2:]
                    binary = self.u.create_eight_digit_bin(binary)
                    red_bin = bin(rgba_show[0])[2:-3]
                    sRed = red_bin + binary[:3]
                    sRed = int(sRed, 2)
                    green_bin = bin(rgba_show[1])[2:-3]
                    sGreen = green_bin + binary[3:6]
                    sGreen = int(sGreen, 2)
                    blue_bin = bin(rgba_show[2])[2:-2]
                    sBlue = blue_bin + binary[6:]
                    sBlue = int(sBlue, 2)
                    stega_img.putpixel((i, j), (sRed, sGreen, sBlue))
                else:
                    stega_img.putpixel((i, j), rgba_show)
        return stega_img


    def merge_image(self, stega_img, img_show, img_hide):
        for i in range(stega_img.width):
            for j in range(stega_img.height):
                rgba_show = img_show.getpixel((i, j))
                rgba_hide = img_hide.getpixel((i, j))
                sRed = self.u.binary_addition_main(rgba_show[0], rgba_hide[0])
                sGreen = self.u.binary_addition_main(rgba_show[1], rgba_hide[1])
                sBlue = self.u.binary_addition_main(rgba_show[2], rgba_hide[2])
                stega_img.putpixel((i, j), (sRed, sGreen, sBlue))
        return stega_img