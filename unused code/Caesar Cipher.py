from alphabet import alphabet
from art import title
from os import system, name

print(title)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alph_len = len(alphabet)

def caesar(text, shift, direction):
    # continue_ = True
    # while continue_:
        word = ""
        word_list = []
        for item in text:
            if item in alphabet:
                letter_index = alphabet.index(item)
                if direction == 'encode':
                    new_index = letter_index + shift
                elif direction == 'decode':
                    new_index = letter_index - shift
                else:
                    print(f"{direction} is an invalid input")
                if new_index > 26:
                    step1 = 0
                    step2 = new_index - alph_len
                    step3 = step1 + step2
                    new_index = step3
                encoded_item = alphabet[new_index]
                word_list.append(encoded_item)
            else:
                word_list.append(item)
        print(f"Your message: \n{word.join(word_list)}") 
        # yes_no = input('Would you like to continue using the Caesar Cipher? ')
        # if yes_no == 'no':
        #     continue_ = False 
        # elif yes_no == 'yes':
        #     continue_ == True
        # else:
        #     print('INVALID INPUT')

# def encrypt(text, shift, direction):
#     word = ""
#     word_list = []
#     for item in text:
#         if item in alphabet:
#             letter_index = alphabet.index(item)
#             new_index = letter_index + shift
#             if new_index > 26:
#                 step1 = 0
#                 step2 = new_index - alph_len
#                 step3 = step1 + step2
#                 new_index = step3
#             encoded_item = alphabet[new_index]
#             word_list.append(encoded_item)
#         else:
#             word_list.append(item)
#     print(f"Your message: \n{word.join(word_list)}")  

# def decrypt():
#     encrypt(text = text, shift = -shift)

def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

# if direction == "encode":
#     encrypt(text = text, shift = shift)
# elif direction == "decode":
#     decrypt()
# else:
#     print(f"{direction} is an invalid input")



   
   

continue_ = True
while continue_ == True:
    caesar(text=text, shift=shift, direction=direction)
    yes_no = input('Would you like to continue using the Caesar Cipher? ')
    if yes_no == 'yes':
        continue_ = True
    elif yes_no == 'no':
        continue_ = False
    else:
        print('INVALID INPUT')

# yes_no = input('Would you like to continue using the Caesar Cipher?')
# if yes_no == 'no':
#     exit
# elif yes_no == 'yes':
#     caesar(text=text, shift=shift, direction=direction)
# else:
#     print('FALSE INPUT')




#NOTES#
#for fewer lines, maybe try combining the encrypt and decrypt functions into one function that does it all, and just takes more arguments.
#use a boolean or while loop or something to allow the user to keep running the program until they are done, 
#and have it clear the terminal when they are done.