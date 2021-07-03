from PIL import Image
import sys
from PIL import ImageColor from steganography import new_image

def left_shift(val):
    return val << 4

def retrieve_image(val):
    val = val << 4
    val = val % 255
    return(left_shift(val >> 4))

def new_func():
    print("Hello")

def decode(decoded_img, img):
    for x in range(img.width):
        for y in range(img.height):
           rbg = img.getpixel((x, y))
           red = retrieve_image(rbg[0])
           green = retrieve_image(rbg[1])
           blue = retrieve_image(rbg[2])
           decoded_img.putpixel((x, y), (red, green, blue))

    return decoded_img


def main():
    print("Do you want to : ")
    print("\t 1. decode an already present image")
    print("\t 2. decode your own image")
    choice = int(input("Enter your choice : "))

    img = Image.open("stegaImage.png")
 
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

        img = Image.open(f"images/{img1}")
    
    if(img == None):
        print("Image not found in the location")
        sys.exit()

    decoded_img = new_image(img.width, img.height)
    decoded_img = decode(decoded_img, img)
    decoded_img.save("decodedImg.png")
    print("\n\t\tDECODED IMAGE HAS BEEN SAVED BY NAME 'decodedImg.png' \n\n")
