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


<<<<<<< HEAD
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
=======

def main():
    print("\t\tTHIS ALGORITHM DOESN'T WORK PROPERLY WITH DARK IMAGES WHILE DECODING THE IMAGE...\n")

    print("Do you want to: ")
    print("\t 1. See the demo with already present images")
    print("\t 2. Enter your own images")
    choice = int(input("Enter your choice : "))

    img_show = Image.open("images/usian.jpg")
    img_hide = Image.open("images/skyline.jpg")

    if(choice == 2):
        print("\t\tAdd images in images folder present in this folder")
        img1 = print("Enter image name with extension that you want to hide (only jpg and png accepted): ")
        img1 = input()

        accepted_ext = ("jpg", "png", "jpeg")

        while(True):
            if(img1.split(".")[1] not in accepted_ext):
                print("File format not accepted...")
            else:
                break

        img2 = print("Enter image name with extension that you want to show : ")
        img2 = input()

             
        while(True):
            if(img1.split(".")[1] not in accepted_ext):
                print("File format not accepted...")
            else:
                break
>>>>>>> 15728ab32ebb0a8431e61961fc425b412710cb89


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