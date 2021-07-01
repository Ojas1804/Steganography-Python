from PIL import Image
from PIL import ImageColor
import math
import sys



def shift(val, img_type):
    if(img_type == 'h'):
        return(math.floor(val >> 4))
    return ((val >> 4) << 4)



def alterShow(img):
    width, heigth = img.size

    for x in range(width):
        for y in range (heigth):
            rgba = img.getpixel((x, y))
            red = shift(rgba[0], 's')
            green = shift(rgba[1], 's')
            blue =  shift(rgba[2], 's')
            img.putpixel((x, y), (red, green, blue))

    return img



def alterHide(img):
    width, height = img.size

    for x in range(width):
        for y in range(height):
            rgba = img.getpixel((x, y))
            red = shift(rgba[0], 'h')
            green = shift(rgba[1], 'h')
            blue = shift(rgba[2], 'h')
            img.putpixel((x, y), (red, green, blue))

    return img



def same_size(img_show, img_hide, width, height):
    img_show = img_show.crop((0, 0, width, height))
    img_hide = img_hide.crop((0, 0, width, height))

    return img_show, img_hide



def new_size(img1, img2):
    new_height = img1.height
    new_width = img1.width
    if(img1.height > img2.height):
        new_height = img2.height
    if(img1.width > img2.width):
        new_width = img2.width

    return new_width, new_height


def new_image(width, height):
    return (Image.new('RGBA', (width, height)))


def binary_addition(x, y):
    return (x | y)



def merge_image(stega_img, img_show, img_hide):
    for i in range(stega_img.width):
        for j in range(stega_img.height):
            rgba_show = img_show.getpixel((i, j))
            rgba_hide = img_hide.getpixel((i, j))
            sRed = binary_addition(rgba_show[0], rgba_hide[0])
            sGreen = binary_addition(rgba_show[1], rgba_hide[1])
            sBlue = binary_addition(rgba_show[2], rgba_hide[2])
            stega_img.putpixel((i, j), (sRed, sGreen, sBlue))
    
    return stega_img



def main():
    print("\t\tTHIS ALGORITHM DOESN'T WORK PROPERLY WITH DARK IMAGES WHILE DECODING THE IMAGE...\n")

    print("Do you want to: ")
    print("\t 1. See the demo with already present images")
    print("\t 2. Enter your own images")
    choice = int(input("Enter your choice : "))

    img_show = Image.open("images/hider.png")
    img_hide = Image.open("images/template.jpg")

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


        img_show = Image.open(f"images/{img2}")
        img_hide = Image.open(f"images/{img1}")

    if(img_show == None):
        print("Image suppsoed to be hide another image is not present in folder")
        sys.exit()

    if(img_hide == None):
        print("Image supposed to be hidden is not present")
        sys.exit()

    img_show = alterShow(img_show)
    img_hide = alterHide(img_hide)


    new_width, new_height = new_size(img_hide, img_show)
    img_show, img_hide = same_size(img_show, img_hide, new_width, new_height)

    stega_img = new_image(new_width, new_height)
    stega_img = merge_image(stega_img, img_show, img_hide)
    stega_img.save("stegaImage.png")
    print("\n\t\tSTEGANOGRAPHIC IMAGE HAS BEEN SAVED BY NAME 'stegaImage.png' \n\n")
