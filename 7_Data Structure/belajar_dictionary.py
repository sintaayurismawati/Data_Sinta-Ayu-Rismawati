simple_dict = {"angka" : 1, "nama" : "Alterra", "status" : True} 
print(simple_dict)
print(simple_dict["angka"])

# add
simple_dict["new"] = 123

#update
simple_dict["angka"] = 2

# delete
del simple_dict["status"]

print(simple_dict)



second_dict = dict([("angka",2), ("nama", "Alterra"), ("status",True)])
print(second_dict)

other_dict = dict({"angka" : 2})
print(other_dict)