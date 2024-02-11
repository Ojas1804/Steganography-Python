from PIL import Image


class Utility:
    def create_eight_digit_bin(binary):
        return ("0"*(8-len(binary)) + binary)
    

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
    
    
    def create_eight_digit_bin(binary):
        return ("0"*(8-len(binary)) + binary)
    
    def binary_addition(x, y):
        x = bin(x)[2:]
        y = bin(y)[2:]
        return int(x[:4]+y[:4], 2)


    def binary_addition_main(x, y):
        return (x|y)