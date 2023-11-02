list = [145, 781, 954, 169, 457, 120, 122, 163, 186, 142]
newList = []
for i in range(0, len(list)):
    newList.append(0)

# print(countList)
def getMax(list):
    comp = list[0]
    for i in range(0,len(list)):
        if(comp<list[i]):
            comp = list[i]
    return comp
   
   
def count_sort(list, place):
    countList = []
    for i in range(0, len(list)):
        countList.append(0)
    
    for i in range(0, len(list)):
        countList[(int(list[i]/place))%10]+=1
    for j in range(1, len(countList)):
        countList[j] = countList[j] + countList[j-1]
    # print(countList)    
    for k in range(len(list)-1,0,-1):
        newList[countList[int((list[k]/place))%10]-1] = list[k]
        countList[(int(list[k]/place))%10]-=1
    for l in range(0, len(newList)):
        list[l] = newList[l]

def radix_sort(list):
    max = getMax(list)
    place = 1
    # while(max !=0):
    count_sort(list, place)
    place *=10
    # max/=10
    count_sort(list, place)
    place *=10
    # # max/=10
    count_sort(list, place)
    place *=10
    # max/=10
radix_sort(list)
print(newList)   
# print(len(list))         
        
        
        
           
    

        
    

