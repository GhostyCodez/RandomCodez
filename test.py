class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return F"{self.name} says {sound}" 
class goldenretriever(Dog): 
    def speak(self, sound="Bark"):
        return f"{self.name} says {sound}"
    
    
miles = JackRussellTerrier("Miles", 4)
buddy = goldenretriever("Buddy", 9)
jack = Dog("Jack", 3)
jim = Dog("Jim", 5)
print(miles.description())
print(miles.speak())
print(buddy.speak())
print(miles)