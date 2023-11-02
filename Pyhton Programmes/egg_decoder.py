
code = input("Enter the code on label: ")

def farming_method_identifier(letter):
    farming_method = {
    "0" : "Organic",
    "1" : "Free Range",
    "2" : "Barn", 
    "3" : "Cage"
    }
    if letter == 0 or 1 or 2 or 3:
        method = farming_method[letter]
    else:
        method = "Invalid Code !"
    return method

def origin_identifier(letter):
    i = 0
    with open("country-codes.txt", "r") as f:
        country = f.readlines()
        while (1):
            line = country[i]
            if line[0:2] == letter:
                break
            i+=1
        line.replace("\n", "")
    return line[3:]

print(farming_method_identifier(code[:1]) +" Egg")
print("Country of Origin " + origin_identifier(code[1:3]))
print("Farm ID " + code[3:])
    
    

        
        

        
    

    
        
            
        
            
        