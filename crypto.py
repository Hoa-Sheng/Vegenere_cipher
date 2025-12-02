text = "cypher"
key = 3
list_of_strings = []

def cesar_cipher(text, key):
    
    for char in text:
        x = chr(ord(char) + key)
        list_of_strings.append(x)
    crypted_text = "".join(list_of_strings)
    return crypted_text

crypted_text = cesar_cipher(text, key)

print(crypted_text)