w=input("ENTER ANY WORD")

for i in w:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        print(i,"IS A VOWEL")
        break
    else:
        print(i,"IS A CONSONANT")