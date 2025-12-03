def cesar_cipher(text, key):
    crypted_text = ""

    for char in text:
        chrypted_char = chr((ord(char) + key % 26))
        crypted_text += chrypted_char

    return crypted_text

print(cesar_cipher("hello", 3))