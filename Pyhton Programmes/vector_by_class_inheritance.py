class C2dVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    
class C3dVector(C2dVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

C2d = C2dVector(4, 6)
print(C2d)
C3d = C3dVector(8, 9, 3)
print(C3d)
                    
    