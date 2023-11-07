import random
import string
import time 

randomLetter = random.choice(string.ascii_letters)
str = 'Honey Parihar'
str1 = ''
i = 0;
while (True):
    word = random.choice(string.ascii_letters)
    print(word)
    print(str1, end = "")
    if word == str[i]:
        str1 += word
        i += 1
    if str[i] == ' ':
        str1 += ' '
        i+=1
    if str == str1:
        break
    
    time.sleep(0.01)
    


