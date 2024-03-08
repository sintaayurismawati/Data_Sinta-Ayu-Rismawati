# polymorphism = kemampuan dr objek dr tipe yg berbeda, untuk merespon fungsi dengan nama yang sama
class Animal : 
    def speak(self) :
        return "..."
    
class Cat(Animal) :
    def speak(self) :
        return "Mewooo"
    
class Anjing(Animal) :
    def speak(self) :
        return "Gukguk"
    
class Bebek(Animal) :
    def speak(self) :
        return "Kwek kwek"
    
print(Cat().speak())
print(Anjing().speak())
print(Bebek().speak())