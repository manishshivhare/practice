para = "Note that in both the approaches above, we've been using the index of the string to iterate over each character. Let's try calling a for-each loop for the purpose"
count = 0
vowel = "a","i","e","o","u"
for elements in para:
    if(elements in vowel):
        count = count+1
print(count)        

    