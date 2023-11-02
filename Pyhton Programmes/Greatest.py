# def great(num1, num2 , num3):
#     if(num1>num2 and num1>num3):
#         return num2
#     elif(num2>num1 and num2>num3):
#         return num2
#     else:
#         return num3
    
# print(great(41, 75, 15))    


def great_array(arr):
    j = 0
    for i in range(1, len(arr), 1):
        if(arr[j]<arr[i]):
            j = i
    return arr[j]
list = [14, 15, 78, 25, 94, 117, 34, 94, 75]
print(great_array(list))      
        