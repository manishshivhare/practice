import csv
# host = [["web", "1540.147.125."],["ssl", "154.154.128.0.0"]]
# with open("host.csv", "w") as server:
#     write = csv.writer(server)
#     write.writerows(host)



# f = open("by.txt")
# csvf = csv.reader(f)
# for row in csvf:
#     a,b = row
#     print(a,b)

# users =[{"user":"Ramoza", "model": "galaxy", "usage": "daily"},
#        {"user":"Nevin", "model": "Iphone", "usage": "once"},
#        {"user":"Rick", "model": "Redmi", "usage": "Usually"}]
# keys = ["user", "model", "usage"]
# with open("dict.csv", "w") as file:
#     writer = csv.DictWriter(file, fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(users)
    
with open("dict.csv") as f:
    read = csv.DictReader(f)
    for row in read:
        print("{} has {} and use {}".format(row["user"], row["model"], row["usage"])) 



