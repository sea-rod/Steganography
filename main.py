from unicodedata import name
from xml.sax.xmlreader import InputSource
import stegano

def hide_message():
    mess = input("Enter the Message You Wanna Hide:")
    path = input("Enter the Image Path:")
    mess = stegano.encode(mess)
    pixel = stegano.reader(path)
    print("-"*34+"Please Wait"+"-"*34,end='\r')
    mat = stegano.encode_pixel(pixel,mess)
    stegano.write_to_img(mat,path)
    print("-"*34+"Complete"+"-"*34)

def decode_message():
    path = input("Enter Image's path:")
    pixel = stegano.reader(path)
    mess = stegano.get_bytestring_from_img(pixel)
    print("The message is:",mess)




if __name__ == "__main__":
    try:
        print("\n\n"+"-"*45+" Welcome To Steganography "+"-"*45)
        ch = int(input("[+] 1.Hide Message in the image\n[+] 2.Decode a Message hidden in the image\n[+] Enter Your Option:"))
        swtch = {1:hide_message,
                 2:decode_message}
        swtch[ch]()
    except ValueError:
        print("Enter a integer")
    except KeyError:
        print("Invalid Choice")