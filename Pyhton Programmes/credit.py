cc = input("Enter CC Number: ")
for x in range(0, (len(cc)-4)):
    cc = cc.replace(cc[x],'*')
print(cc)
