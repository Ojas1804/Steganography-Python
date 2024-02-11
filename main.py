import sys
from steganography import Steganography
from decode_stega import Decoder
import Utility
from PIL import Image

s = Steganography()
d = Decoder()
u = Utility

def hide_image():
    ut = Utility()
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
                sys.exit()
            else:
                break
        img2 = print("Enter image name with extension that you want to show : ")
        img2 = input()
        while(True):
            if(img1.split(".")[1] not in accepted_ext):
                print("File format not accepted...")
                sys.exit()
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
    img_show = ut.alterShow(img_show)
    img_hide = ut.alterHide(img_hide)

    new_width, new_height = ut.new_size(img_hide, img_show)
    img_show, img_hide = ut.same_size(img_show, img_hide, new_width, new_height)

    stega_img = ut.new_image(new_width, new_height)
    s = Steganography()
    stega_img = s.merge_image(stega_img, img_show, img_hide)
    stega_img.save("stegaImage.png")
    print("\n\t\tSTEGANOGRAPHIC IMAGE HAS BEEN SAVED BY NAME 'stegaImage.png' \n\n")


def hide_text():
    print("Do you want to: ")
    print("\t 1. See the demo with already present images")
    print("\t 2. Enter your own image and text")
    choice = int(input("Enter your choice : "))
    img_show = Image.open("images/usain.jpg")
    text = "This is sample text"
    text_len = str(len(text))
    text = text_len + ":" + text
    if choice == 2:
        text = input("Enter text : ")
        print("\t\tAdd images in images folder present in this folder")
        img1 = print("Enter image name with extension that you want to hide (only jpg and png accepted): ")
        accepted_ext = ("jpg", "png", "jpeg")

        while(True):
            if(img1.split(".")[1] not in accepted_ext):
                print("File format not accepted...")
                sys.exit()
            else:
                break
        img_show = Image.open(f"images/{img1}")
    if(img_show == None):
        print("Image suppsoed to be shown another image is not present in folder")
        sys.exit()
    img_show = s.alterShow(img_show)
    stega_img = u.new_image(img_show.width, img_show.height)
    print(stega_img.size)
    stega_img = s.merge_image_text(stega_img, img_show, text)
    print(stega_img.size)
    stega_img.save("stegaImageText.png")
    print("\n\t\tSTEGANOGRAPHIC IMAGE HAS BEEN SAVED BY NAME 'stegaImageText.png' \n\n")
    print(decode_text(stega_img))


def decode_image():
    print("Do you want to : ")
    print("\t 1. decode a demo image")
    print("\t 2. decode your own image")
    choice = int(input("Enter your choice : "))

    img = Image.open("stegaImageText.png")
 
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
    decoded_img = u.new_image(img.width, img.height)
    decoded_img = d.decode_image(decoded_img, img)
    decoded_img.save("decodedImg.png")
    print("\n\t\tDECODED IMAGE HAS BEEN SAVED BY NAME 'decodedImg.png' \n\n")


def decode_text():
    print("Do you want to : ")
    print("\t 1. decode text from a demo image")
    print("\t 2. decode text from your own image")
    choice = int(input("Enter your choice : "))
    img = Image.open("stegaImageText.png")
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
    text = d.decode_text(img)
    print(f"DECODED TXT: {text}")


def main():
    while(True):
        print("Do you want to : ")
        print("\t 1. Hide an image")
        print("\t 2. Hide an image")
        print("\t 3. Decode an image")
        print("\t 4. Decode an image")
        print("\t Press any other number to exit")

        choice = int(0)
        try:
            choice = int(input("Enter your choice : "))
        except Exception as e:
            print(f"Error Msg : {e}")

        if(choice == 1):
            hide_image()

        elif(choice == 2):
            hide_text()

        elif(choice == 3):
            decode_image()
        
        elif(choice == 4):
            decode_text()

        else:
            sys.exit()
