s=list(input('enter a string of numbers and letters: ',))
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def count_tenz(s):
    print(s)
    new_s=[]
    string_length=len(s)
    tenz=[]
    for digit in s:
        if digit in numbers:
            new_s.append(int(digit))
        else:
            new_s.append(digit)
    for digit in range(0,string_length-1):
        if isinstance(new_s[digit], int) and isinstance(new_s[digit+1], int) and not isinstance(new_s[digit+2],int) and not new_s[digit]==0:
            tenz.append(str(new_s[digit])+str(new_s[digit+1]))
    #if isinstance(new_s[string_length], int) and isinstance(new_s[string_length-1], int) and isinstance(new_s[string_length-2], int):
       # del tenz[-1]
    print(tenz)
    print("DOOOOOOORPPPPP")

count_tenz(s)