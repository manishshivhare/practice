
def donkey():
    with open("donkey.txt") as f:
        content = f.read()
    content = content.replace("donkey", "#$%^^%$#")
    with open("donkey.txt", "w") as f:
        f.write(content)    
        
donkey()        
   
   