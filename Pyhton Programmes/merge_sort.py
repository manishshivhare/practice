newList = []
def merge_list(list, start, mid, end):
    i = start
    j = end 
    k =0
    
    while(i<mid and j<end):
        if(list[i]>list[j]):
            newList[k] = list[j]
            j+=1
        else:
            newList[k] = list[i]
            i+=1
        k+=1
    while(i<mid):
        newList[k] = list[i]
        i+=1
        k+=1        
    while(j<end):
        newList[k] = list[j]
        j+=1
        k+=1        
    
def partition(list, start, end):
    if(start<end):
        mid = (start + end)/2
        partition(list, start, mid)
        partition(list, mid+1, end)
        merge_list(list, start, mid, end)
        
        
list = {12, 78, 45, 14, 94, 75, 26, 19, 34, 29, 37, 10}

partition(list, 0, len(list)-1)
print(newList)