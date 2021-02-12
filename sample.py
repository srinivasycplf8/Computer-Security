from Crypto.Cipher import AES
import binascii


class AESCipher(object):
    def __init__(self, file_name,given_cipher):
        self.block_size = AES.block_size
        self.file_name = file_name
        self.given_cipher=given_cipher

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        with open(self.file_name) as f:  
            words=[]

            white_space=" "

            new_line="\n"

            for each in f:

                if each is not white_space:

                    words.append(each.lower())
        
        words=list(map(lambda x:x.strip(),words))

        iv = bytes.fromhex('010203040506070809000a0b0c0d0e0f').decode("ISO-8859-1")
        for key in words:
            if len(key)<16:
                key=key+"#"*(16-len(key))     
                cipher = AES.new(key.encode("ISO-8859-1"), AES.MODE_CBC, iv.encode("ISO-8859-1"))
                encrypted_text = cipher.encrypt(plain_text.encode())
                cipher_hex=binascii.hexlify(encrypted_text)
                if self.given_cipher==cipher_hex.decode("ISO-8859-1"):
                    print("Solution of the key is :",key)
                    return



    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text





x=AESCipher("words.txt","e5accdb667e8e569b1b34f423508c15422631198454e104ceb658f5918800c22")
print(x.encrypt("This is a top secret."))

