class Vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str = ""
        index = 0
        for i in self.vec:
            str+= f"{i}a{index} +"
            index+=1
        return(str[:-1])
    def __add__(self, vec1):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec1.vec[i])
        return Vector(newList)
    
vector1 = Vector([1, 8, 6, 7])
vector2 = Vector([3, 7, 3, 2])
print(vector2 + vector1)



