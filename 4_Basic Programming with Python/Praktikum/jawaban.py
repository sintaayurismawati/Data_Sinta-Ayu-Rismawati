
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