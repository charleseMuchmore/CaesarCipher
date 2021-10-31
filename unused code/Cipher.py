title = '''
 __          __  _                            _           _____                             _____ _       _                
 \ \        / / | |                          | |         / ____|                           / ____(_)     | |               
  \ \  /\  / ___| | ___ ___  _ __ ___   ___  | |_ ___   | |     __ _  ___ ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __  
   \ \/  \/ / _ | |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |    / _` |/ _ / __|/ _` | '__| | |    | | '_ \| '_ \ / _ | '__| 
    \  /\  |  __| | (_| (_) | | | | | |  __/ | || (_) | | |___| (_| |  __\__ | (_| | |    | |____| | |_) | | | |  __| |    
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \_____\__,_|\___|___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|    
                                                                                                   | |                     
                                                                                                   |_|                     
'''                                                              
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']                                     
from os import system, name
print(title)
alph_len = len(alphabet)
def caesar(text, shift, direction):
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
                if new_index >= 26:
                    step1 = 0
                    step2 = new_index - alph_len
                    step3 = step1 + step2
                    new_index = step3
                encoded_item = alphabet[new_index]
                word_list.append(encoded_item)
            else:
                word_list.append(item)
        print(f"Your message: \n{word.join(word_list)}") 
def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')
continue_ = True
while continue_ != False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    yes_no = input('Would you like to continue using the Caesar Cipher? ').lower()
    if yes_no == 'yes' or 'y':
        continue_ = True
    elif yes_no == 'no' or 'n':
        clear()
        continue_ = False
    else:
        print('INVALID INPUT')

#NOTES#
#for fewer lines, maybe try combining the encrypt and decrypt functions into one function that does it all, and just takes more arguments.
#use a boolean or while loop or something to allow the user to keep running the program until they are done, 
#and have it clear the terminal when they are done.