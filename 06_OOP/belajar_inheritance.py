# INHERITANCE
# SUPER : digunakan method yang sudah ada dari kelas induk
# Mthod override : menggunakan method dr kelas induk dan menambahkan logika sesuai kebutuhan

class Person :
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def indentify(self):
        return self.first_name + " " + self.last_name
    
class Employee(Person):
    def __init__(self, first_name, last_name, staff_number):
        super().__init__(first_name, last_name)
        self.staff_number = staff_number
    def indentify(self):
        return super().indentify() + " " + str(self.staff_number)

# membuat 2 objek dari kelas person dan employee
person_budi = Person("Budi", "Purnama")
employee_budi = Employee("Budi", "Purnama", 19821)

# memanggil method identify dari kelas person
identity_person_budi = person_budi.indentify()
print(identity_person_budi)

# memanggil method identify dari kelas employee
identity_employee_budi = employee_budi.indentify()
print(identity_employee_budi)