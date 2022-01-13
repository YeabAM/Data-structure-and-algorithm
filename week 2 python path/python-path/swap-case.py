def swap_case(s):
    word=list(s)
    for letter in range(len(word)):
        if word[letter].isupper():
            word[letter] = word[letter].lower()          
        else:
            word[letter] = word[letter].upper()
    s=''.join(map(str, word))        
    return s


if __name__ == '__main__':
