VOWELS=set()
CONBM=set()
CONNZ=set()
CONSONANTS=set()
PAIRS=set()
BANKV=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
BANKCBM=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M']

def letters_sets(n):
    list_of_strings = []
    for i in range(n):
        list_of_strings.append(input("input another string"))

    for string in list_of_strings:
        for letter in string:
            if letter in BANKV:
                VOWELS.add(letter)
            elif letter in BANKCBM or letter.upper() in BANKCBM:
                CONBM.add(letter)
                CONSONANTS.add(letter)
            else:
                CONNZ.add(letter)
                CONSONANTS.add(letter)
                CONNZ.discard(" ")
                CONSONANTS.discard(" ")
    for string in list_of_strings:
        len_string = len(string)
        for j in range(0, len_string - 1):
           if string[j] in BANKV and string[j+1] not in BANKV:
               vowel_consonant_pair = string[j] + string[j+1]
               PAIRS.add(vowel_consonant_pair)
           if string[j] not in BANKV and string[j+1] in BANKV:
               consonant_vowel_pair = string[j] + string[j+1]
               PAIRS.add(consonant_vowel_pair)
                
            
            

n=int(input('enter the number of strings to input: '))
letters_sets(n)
print(VOWELS)
print(CONBM)
print(CONNZ)
print(PAIRS)