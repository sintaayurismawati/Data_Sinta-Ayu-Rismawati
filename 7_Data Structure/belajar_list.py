list_number = [1,2,3,4,5]
print(list_number)
print(list_number[1:3])
print(list_number[1:])
print(list_number[:3])
print(len(list_number))

list_string = ["Bandung", "Jakarta", "Surabaya"]
list_string.append("Solo")
print(list_string)
print(list_string[0])
print(list_string[-1])

list_mixed = [1, "Bandung",True, "Bandung"]
list_mixed.insert(1,False)
print(list_mixed)
list_mixed.remove("Bandung")
list_mixed.pop(0)
del list_number[2]

