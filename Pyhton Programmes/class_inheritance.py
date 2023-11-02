class Employee:
    salary = 5600
    bonus = 200
    
    @property
    def getSalary(self):
        return (self.salary + self.bonus)
    
    @getSalary.setter
    def getSalary(self, val):
        self.bonus = val - self.salary
        
e = Employee()
e.getSalary = 5700
print(e.bonus)
        
        