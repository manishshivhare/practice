
listA = []
n = int(input("size of list: "))
for i in range(0, n):
    print("Enter element-{}: ".format(i+1))
    elem = int(input())
    listA.append(elem)
print("for ascending enter asc and desc for descending order")
choice = input()
if(choice == "desc"):
    listA.sort(reverse=True)
else:
    listA.sort()
print(listA)
    