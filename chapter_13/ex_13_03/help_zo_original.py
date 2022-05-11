VOWELS=set()
CONBM=set()
CONNZ=set()
CONSONANTS=set()
PAIRS=set()
BANKV=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
BANKCBM=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M']

def letters_sets(n):
    for i in n:
        for j in i:
            if j in BANKV:
                VOWELS.add(j)
            elif j in BANKCBM or j.upper() in BANKCBM:
                CONBM.add(j)
                CONSONANTS.add(j)
            else:
                CONNZ.add(j)
                CONSONANTS.add(j)
                CONNZ.discard(" ")
                CONSONANTS.discard(" ")
    for string in n:
        length_of_string = len(n)
        for letter in range(0,l):
           if n[j] in BANKV and n[j+1] not in BANKV:
               g=n[j]+n[j+1]
               PAIRS.add(g)
           if n[j] not in BANKV and n[j+1] in BANKV:
               h=n[j]+n[j+1]
               PAIRS.add(h)
                
            
            
            

n=input('enter stings of letter',)
letters_sets(n)
print(VOWELS)
print(CONBM)
print(CONNZ)
print(PAIRS)