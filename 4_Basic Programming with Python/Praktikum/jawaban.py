# PRIORITAS 1
# No.1
panjnag = input("Masukkan panjang : ")
lebar = input("Masukkan lebar : ")
p = int(panjnag)
l = int(lebar)
luas = p * l
if luas % 2 == 0 :
    print("even rectangle")
else :
    print("odd rectangle")

# PRIORITAS 1
# No.2
jarijari = input("Masukkan jari-jari : ")
r = int(jarijari)
volume = 4/3 * 3.14 * r**3
print("Volume tabung : ", volume)

# PRIORITAS 1
# No.3
for x in range(1, 101) :
    if x % 3 == 0 and x % 5 == 0 :
        print("buzz")
    elif x % 3 == 0 :
        print(x**2)
    elif x % 5 == 0 :
        print(x**3)
    else :
        print(x)

# PRIORITAS 2
# No.1
beratBarang = input("Masukkan berat : ")
jarakTempuh = input("Masukkan jarak : ")
berat = int(beratBarang)
jarak = int(jarakTempuh)

if berat <= 20 :
    tarifBerat = 10000
elif berat <= 30 :
    tarifBerat = 15000
elif berat <= 60 :
    tarifBerat = 20000
elif berat > 60 :
    tarifBerat = 45000

if jarak <= 5 :
    tarifJarak = 2000
elif jarak <= 15 :
    tarifJarak = 5000
elif jarak <= 30 :
    tarifJarak = 10000
elif jarak > 30 :
    tarifJarak = 15000

totalTarif = tarifBerat + tarifJarak
print("Tarif pengiriman : ", totalTarif)

# PRIORITAS 2
# No.2
budgetProyek = input("Masukkan budget : ")
waktuKerja = input("Masukkan waktu pengerjaan : ")
tingkatKesulitan = input("Masukkan tingkat kesulitan : ")
budget = int(budgetProyek)
waktu = int(waktuKerja)
kesulitan = int(tingkatKesulitan)

if budget <= 50 :
    skorBudget = 4
elif budget <= 80 :
    skorBudget = 3
elif budget <= 100 :
    skorBudget = 2
elif budget > 100 :
    skorBudget = 1

if waktu <= 20 :
    skorWaktu = 10
elif waktu <= 30 :
    skorWaktu = 5
elif waktu <= 50 :
    skorWaktu = 1
elif waktu > 10 :
    skorWaktu = 0

if kesulitan <= 3 :
    skorSulit = 10
elif kesulitan <= 6 :
    skorSulit = 5
elif kesulitan <= 10 :
    skorSulit = 1
elif kesulitan > 10 :
    skorSulit = 0

skorTotal = skorBudget + skorWaktu + skorSulit
if 17 <= skorTotal <= 24 :
    print("High")
elif 10 <= skorTotal <=16 :
    print("Medium")
elif 3 <= skorTotal <= 9 :
    print("Low")
elif skorTotal <=2 :
    print("Impossible")