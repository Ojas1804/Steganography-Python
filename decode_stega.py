class Decoder:
    def left_shift(self, val):
        return val << 4

    def retrieve_image(self, val):
        val = val << 4
        val = val % 255
        return(self.left_shift(val >> 4))

    def retrieve_text(self, val, color):
        binary = bin(val)[2:]
        if color=='r':
            return binary[-3:]
        if color=='g':
            return binary[-3:]
        return binary[-2:]


    def decode_image(self, decoded_img, img):
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                rbg = img.getpixel((x, y))
                red = self.retrieve_image(rbg[0])
                green = self.retrieve_image(rbg[1])
                blue = self.retrieve_image(rbg[2])
                decoded_img.putpixel((x, y), (red, green, blue))
        return decoded_img


    def decode_text(self, img):
        first_colon = False
        text_len = -1
        decoded_string = ""
        text_len_string = ""
        i = 0
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                rbg = img.getpixel((x, y))
                red = str(self.retrieve_text(rbg[0], 'r'))
                green = str(self.retrieve_text(rbg[1], 'g'))
                blue = str(self.retrieve_text(rbg[2], 'b'))
                ascii_val = red+green+blue
                ascii_val = int(ascii_val, 2)
                if not first_colon:
                    if chr(ascii_val) == ':':
                        text_len = int(text_len_string)
                        first_colon = True
                        print(f"text length: {text_len}")
                    else:
                        text_len_string += chr(ascii_val)
                else:
                    if i < text_len:
                        decoded_string += chr(ascii_val)
                        i+=1
                    else:
                        return decoded_string
        return None