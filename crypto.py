text = "cyphers are fun!"
key = 3
list_of_strings = []

def cesar_cipher(text, key):

    for char in text:
        x = chr(ord(char) + key)
        list_of_strings.append(x)
    crypted_text = "".join(list_of_strings)
    return crypted_text

def vigenere_cipher(text, key):

    key = key.lower()
    text = text.lower()
    list_of_key = []
    list_of_text = []
    list_of_A = []
    list_of_text_encrypted = []
    len_text = 0

    # Pour la clé, on la transforme en liste de nombres ascii
    for char in key :
        key_numbers = ord(char)
        list_of_key.append(key_numbers)
        len_key = len(list_of_key)

    for s in text:
        if s.isalpha():
            len_text += 1
    len_text_string = len(text)
    # pour le texte, on transforme en liste de nombres ascii
    for char in text :

        text_numbers = ord(char)
        list_of_text.append(text_numbers)
    
    #Créé une liste de la taille du texte avec la clé de A répété

    for i in range(len_text) :
        list_of_A.append(ord('a'))
        
    if len_text < len_key :

        while len(list_of_key) != len_text :
            list_of_key = list_of_key[:-1]

    elif len_text >= len_key :

        while len(list_of_key) < len_text :

            for j in range(len_key) :
                list_of_key.append(list_of_key[j])

                if len(list_of_key) == len_text :
                    break

    for j in range(len_text) :
        list_of_key[j] -= list_of_A[j]
    
    for j in range(len_text) :
        if list_of_text[j] < 97 or list_of_text[j] > 122 :
            continue
        else :
            list_of_text[j] += list_of_key[j]
        if list_of_text[j] > 122 :
            list_of_text[j] = list_of_text[j] - 26

    for char in list_of_text :
        letter_encrypted = chr(char)
        list_of_text_encrypted.append(letter_encrypted)
    crypted_text = "".join(list_of_text_encrypted)



    return crypted_text

key = 'hoa'
crypted_text = vigenere_cipher(text, key)


print(crypted_text)



# key => le crée en liste, transformer la liste ascii, le faire avoir la meme taille que text avec les répetitions (len) 