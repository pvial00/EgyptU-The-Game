# by Uvajda (Karl Zander) - KryptoMagick 2021

''' EgyptU game0 version AA '''

version = "AA"

class Record:
    text ={}
    keys = {}
    modulus = 0
    mask = 0
    result = {}
    path = {}

def _file_reader(filename, record):
    fd = open(filename, "r")
    data = fd.read()
    fd.close()
    textline = data.split('\n')[0]
    keyline = data.split('\n')[1]
    text = textline.split()
    key = keyline.split()
    textline_len = len(textline)
    
    for c in range(textline_len):
        record.text[c] = textline[c]
        record.keys[c] = keyline[c]
    return record

def _alphabet_generatorB(n):
    alphabet = {}
    alphabet_list = []
    for c in range(n):
        x = c % 26
        letter = chr(x  + 65)
        alphabet[x % 13] = letter
        alphabet_list.append(letter)
    return alphabet, alphabet_list

def _alphabet_generatorBA(n):
    alphabet = {}
    alphabet_list = []
    for c in range(n):
        x = c % 26
        letter = chr(x  + 65 + 13)
        alphabet[x % 13] = letter
        alphabet_list.append(letter)
    return alphabet, alphabet_list

def _alphabet_generatorB(n):
    alphabet = {}
    alphabet_list = []
    for c in range(n):
        x = c % 26
        letter = chr(x  + 65)
        alphabet[x % 14] = letter
        alphabet_list.append(letter)
    return alphabet, alphabet_list

def _alphabet_generatorA(n):
    alphabet = {}
    alphabet_list = []
    for c in range(n):
        x = c % 26
        letter = chr(x  + 65 + 13)
        alphabet[x % 14] = letter
        alphabet_list.append(letter)
    return alphabet, alphabet_list

def run():
    side0B_alphabet, side0B_chars = _alphabet_generatorB(13)
    print(side0B_chars)
    side0BA_alphabet, side0BA_chars = _alphabet_generatorBA(13)
    print(side0BA_chars)

    together = []
    together.extend(side0B_chars)
    together.extend(side0BA_chars)
    print("\n")
    print(together)
    
run()
