class car: 
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage 

    def description(self): 
        return f"The {self.color} car has {self.mileage} miles."

a  = car("blue", 20000)
two = car("red", 30000)  
print(a.description())