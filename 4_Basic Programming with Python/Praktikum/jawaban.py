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