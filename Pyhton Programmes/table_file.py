i = 0
def table(start, end):
    for j in range(start, end+1):
        for i in range(1, 11):
            with open("table_of_{}.txt.".format(j), "a") as f:
                f.write("\n{} X {} = {}".format(j, i, j*i))
    
table(2, 5)





