'''

Challenge #3.

The Caesar Cipher

Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
for extra credit, add a "decrypt" function to your program!

'''

#Define two global alphabet lists for lower and upper case.
plain_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

plain_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_cipher(phrase, shift):
    ''' (str, int) -> str 

        Return the original phrase as a cipher text using the shift to specify
        how many letters ahead to shift in the alphabet.

        Then append the result to the cipher_text.
    '''

    cipher_text = ""
    
    for i in phrase:

        if(not i.isspace() and not i.isdigit() and i.isalpha()):

            if i.isupper():
                cipher_text = cipher_text + plain_upper[((plain_upper.index(i) + shift) % 26)]
            else:
                cipher_text = cipher_text + plain_lower[((plain_lower.index(i) + shift) % 26)]
        
        elif(i.isspace()):
            cipher_text = cipher_text + " "

    return cipher_text

def decrypt_cipher(cipher_text, shift):
    ''' (str, int) -> str
        
        Decrypt the cipher text based on the shift key and return the original
        plain_text.
    '''

    plain_text = ""

    for i in cipher_text:

        if(not i.isspace() and not i.isdigit() and i.isalpha()):

            if i.isupper():
                plain_text = plain_text + plain_upper[(( (plain_upper.index(i) - shift) + 26) % 26 ) ]
            else:
                plain_text = plain_text + plain_lower[(( (plain_lower.index(i) - shift) + 26) % 26 ) ]

        elif(i.isspace()):
            plain_text = plain_text + " "
    
    return plain_text    

print (encrypt_cipher('tHis is a test', 3)) 

print (decrypt_cipher(encrypt_cipher('tHis is a test', 3), 3))

# Completed and working with decrypt function bonus.
