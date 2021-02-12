from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad, unpad

def aes_key(file_name):
    cipher_hex="062ff0112cb32d04d0adcfa02d215abd40a5f932da1ebbd3744de5d16be5a4d7"
    iv = "aabbccddeeff00998877665544332211"
    with open(file_name) as f:  
        words=[]

        white_space=" "

        new_line="\n"

        for each in f:

            char = ""

            for i in range(len(each)): 

                if each[i].isalnum():   
                    char += each[i]

                else:

                    if len(char)>0:     

                        #print(char)

                        words.append(char)
                        #print(len(char)+"fdjf"+print(words))
                        char = ""
                    if each[i] not in white_space and each[i] not in new_line:  
                        words.append(each[i])
    iiv =  bytearray.fromhex("010203040506070809000a0b0c0d0e0f").decode()
    obj = AES.new('example#########'.encode("utf8"), AES.MODE_CBC, iiv.encode("utf8"))
    message = "This is a top secret."
    ciphertext = obj.encrypt(pad(message.encode("utf8"),16))
    cipher_hex=binascii.hexlify(ciphertext)

    print(cipher_hex)
    

file_name=input()
aes_key(file_name)