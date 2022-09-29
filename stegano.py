from ast import main
import png
import base64

ENDOFMESS= "0100100100110000010101100100111101010010010001010011100101000111010101000101010101010110010101000101010101111001010011010011110100001010"


def encode(wrd:str):
    wrd = base64.encodebytes(wrd.encode())
    wrd = "".join(["{:08b}".format(x) for x in wrd])
    return wrd + ENDOFMESS

def reader(name):
    img = png.Reader(name).read()
    return img[2]

def encode_pixel(pixels,bmess):
    enc_pixel = []
    bmess_len = len(bmess)    
    ctr = 0
    for row in pixels:
        enc_row = []
        for pix in row:
            if ctr >= bmess_len:
                enc_row.append(pix)
            else:
                if pix % 2 != int(bmess[ctr]):
                    if pix == 0:
                        enc_row.append(1)
                    else:
                        enc_row.append(pix - 1)
                else:
                    enc_row.append(pix)
            ctr += 1

        enc_pixel.append(enc_row)
    return enc_pixel 


def write_to_img(maxtrix,name:str):
    png.from_array(maxtrix,"RGBA").save(name)


def get_bytestring_from_img(pixels):
    bytestring = []
    for row in pixels:
        for pix in row:
            bytestring.append(str(pix % 2))
    bytestring = "".join(bytestring)
    
    decoded_mess = decode_mess(bytestring)
    return decoded_mess

def decode_mess(bmess):
    bmess = bmess.split(ENDOFMESS)[0]
    mess = int(bmess,2).to_bytes(len(bmess) // 8,byteorder="big")
    mess = base64.decodebytes(mess)
    return mess.decode()


