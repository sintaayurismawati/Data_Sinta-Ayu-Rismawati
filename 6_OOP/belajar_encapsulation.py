# ENCAPSULATION
# contoh membuat class
class ClassRobot :
    pass

# instance
class Cat :
    def __init__(self, fur_color="No Name", num_of_leg=4):
        self._fur_color = fur_color
        self.num_of_leg = num_of_leg

manis = Cat("Hitam", 4)

class Mobil :
    def __init__(self, tipe, name, roda, platnum):
        self.roda = roda
        # protected
        self._type = tipe
        # private
        self.__name = name
        self.__platnum = platnum

class Bebek :
    def speak(self, bunyi_suara):
        return bunyi_suara
    
# membuat objek dari kelas bebek
donald = Bebek()

# memanggil method speak
suara_donald = donald.speak("Kwek kwek")
print(suara_donald)