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





def vigenere_cipher(text, password) :
    list_of_keys = [ord(char) for char in password]
    crypted_text = ""

    for index, char in enumerate(text):
        current_key = list_of_keys[index % len(list_of_keys)]
        crypted_char = cesar_cipher(char, current_key)
        crypted_text += crypted_char
        
    return crypted_text

print(brute_force_cesar_cipher('lhbgdk'))