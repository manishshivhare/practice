# def pattern(n):
#     for i in range(n):
#             print("* ", end= "")
#     print("\n")
#     if(n != 0):
#         pattern(n-1)
# pattern(5)

# def table(num, i, j):
#     print("{} X {} = {}" .format(num, i, num*i))
#     if (i != j):
#         table(num, i+1, j)
# table(12, 1, 15)

def tables(start, end):
    for i in range(1, 11):
        print("{} X {} = {}" .format(start, i, start * i))
    if(start != end):
        tables(start+1, end)
tables(2, 10)


