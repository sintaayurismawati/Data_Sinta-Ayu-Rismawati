SUMMARY - Basic Programming with Python

## Apa itu Python?
Python adalah bahasa pemrograman populer  yang diciptakan oleh Guido van Rossum. Python dirancang untuk mudah dibaca sehingga programmer dapat membuat program yang mudah dipahami.Biasanya digunakan dalam berbagai bidang, antara lain : 
- Pengembangan web (server-side)
- Matematika
- Penulisan skrip sistem
- Membangun alur kerja ( workflow) bersama dengan perangkat lunak lainnya 
- Terhubung dengan sistem database dan modifikasi file
- Menghandle data besar dan melakukan peritungan matematika kompleks 
- Membuat prototipe dengan cepat atau mengembangkan perangkat lunak siap produksi (desktop, mobile, dll)

## Mengapa Python?
- Berjalan di berbagai platform seperti Windows, Mac, Linux dan Raspberry Pi
- Sintaks mudah dipahami , mirip bahasa inggris
- Memungkinkan penulisan program dengan jumlah baris yang lebih sedikit dibanding bahasa pemrograman lainnya
- Dapat dijalankan secara interaktif, memungkinkan prototyping cepat

## Tipe Data di Python 
**1. Numeric**
- Integer, ex :
myint = 7
print(myint)

- Float, ex :
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

**2. String**
Ex : 
mystring = 'hello'
print(mystring)

mystring2 = "UPN 'Veteran' Jawa Timur"
print(mystring2)

**Boolean**Boolean**
Ex : 
mybool = True
print(mybool)

a = True
b = False 

result_and = a and b
result_or = a or b
result_not = not a

print(result_and) --> False
print(result_or) --> True
print(result_not) --> False

## Operator dalam Python
**Arithmetic** : +, -, *, /, %, **
**Assignment** : =, +=, -=, *=, /=, %=, <<=, >>=, &=, ^=, |=
**Comparison** : ==, !=, >, <, >=, <=
**Logical** : and, or, not
**Bitwise** : &, |, ^, <<, >>

## Reading Input
Ex :
user_name = input("Enter username : ")
user_str = string(user_name)
print("You entered : ", user_str)

## IF, ELSE IF, ELSE
Ex :
hour = 15

if hour < 12:
    print("Selamat Pagi"agi")
elif hour < 17:
    print("Selamat Siang")
else:
    print("Selamat Malam")

## Nested If Statement
var v1 int = 400
var v2 int = 700

if v1 == 400 {
    if v2 == 700 {
        fmt.Printf("Value of v1 is 400 and v2 is 700\n");
    }
}

## Looping
for x in range(5) :
print(x) --> 0,1,2,3,4

for x in range(3, 6): 
print(x) --> 3, 4, 5

for x in range(3, 8, 2):
print(x) --> 3, 5, 7

count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
print(count) --> 0,1,2,3,4
count += 1
if count >= 5:
    break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x) --> 1,3,5,7,9

## Nested Looping, Ex :
N = 5

for i in range(N) :
    for j in range (N) :
        print("*", end="")
print()

for i in range (N) :
    for j in range (i + 1) : 
        print("*", end="")
    print()

## Loops Over String
Ex :
sentence = "Hello"
for i in range(len(sentence)) :
    print(sentence[i])

for pos, char in enumerate (sentence) :
    print(f"character {char} starts at byte position {pos}")

## f(x) function
- Function With Parameter, Ex :
--> define function 
def my_function() :
    print("Hello from a function")

def my_function_with_args(username,greeting) :
    print("Hello, %s , From My Function!, I wish you %s"% (username,greeting))

--> call function
my_function()
my_function_with_args("Sinta", "always happy!")

- Function With Return Value, Ex :
def sum_two_numbers(a, b):
return a + b
x = sum_two_numbers(1,2)
print(x)

## List / Array, Ex :
myList =[]
mylist.append(1)
mylist.append(2)
print(mylist[0]) --> 1
print(mylist[1]) --> 2

for x in mylist:
    print(x) --> 1,2