dec = int(input("Enter number: "))
binary, place = 0, 1

while (dec):
    rem=int(dec % 2)
    dec /= 2
    binary=int(binary + (place * rem))
    place *= 10
print(binary)
