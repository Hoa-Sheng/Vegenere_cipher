import string

def cesar_cipher(text, key, cipher = True):

    crypted_text = ""
    
    key = key if cipher else -key #terary

    for char in text:
        crypted_char = chr((ord(char) + key) % 1_114_112)
        crypted_text += crypted_char

    return crypted_text


def brute_force_cesar_cipher(text):
    for key in range(1, 1_114_112):
        potential_initial_text = cesar_cipher(text, key, cipher=False)

        for char in potential_initial_text:
            if char in string.printable:
                print(key)
                print(potential_initial_text)
                print("-------------------")
            break

        
    return





def vigenere

print(brute_force_cesar_cipher('lhbgdk'))