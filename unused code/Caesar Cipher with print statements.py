alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alph_len = len(alphabet)

def encrypt(text, shift):
    word = ""
    word_list = []
    for item in text:
        if item in alphabet:
            # print("\n")
            # print(f"index = {item}")
            letter_index = alphabet.index(item)
            # print(f"original index is: {letter_index}")
            new_index = letter_index + shift
            # print(f"the new index before is: {new_index}")
            if new_index > 26:
                # step1 = alph_len - alph_len
                step1 = 0
                # print(f"{alph_len} - {alph_len} = {step1}")
                step2 = new_index - alph_len
                # print(f"{new_index} - {alph_len} = {step2}")
                step3 = step1 + step2
                # print(f"{step1} + {step2} = {step3}")
                new_index = step3
            encoded_item = alphabet[new_index]
            # print(f"The encoded_item is '{encoded_item}'")
            word_list.append(encoded_item)
        else:
            # print (f"encoded text is '{item}'")
            word_list.append(item)
    print(f"Your message: \n{word.join(word_list)}")
        
def decrypt():
    encrypt(text = text, shift = -shift)

if direction == "encode":
    encrypt(text = text, shift = shift)
elif direction == "decode":
    decrypt()
else:
    print(f"{direction} is an invalid input")
    
# encrypt(text = text, shift = shift)
# decrypt()
