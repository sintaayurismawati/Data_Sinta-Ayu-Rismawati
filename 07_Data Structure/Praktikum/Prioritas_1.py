# No.1
print("NO.1")
def group_numbers(numbers, target) :
    kelipatan = []
    bukanKelipatan = []
    for i in range(len(numbers)) :
        if numbers[i] % target == 0 :
            kelipatan.append(numbers[i])
            i+=1
        else :
            bukanKelipatan.append(numbers[i])
            i+=1
    return[kelipatan, bukanKelipatan]

print(group_numbers([1,2,3,4,5,6,7,8,9],3))
print(group_numbers([23,15,19,20,75,30,45],5))

# No.2
print("\nNO.2")
def get_breads(breads, flour_stock) :
    breads_used = []
    flour_used = 0
    bread_sorted = sorting_breads(breads)
    for i in range(len(bread_sorted)) :
        if flour_used + bread_sorted[i]["flour"] <= flour_stock:
            flour_used += bread_sorted[i]["flour"]
            breads_used.append(bread_sorted[i]["name"])
    return breads_used

def sorting_breads(breads_list):
    sorted_breads = sorted(breads_list, key=lambda x: x["flour"])
    return sorted_breads

bread1 = [
    {"name": "donut", "flour": 25},
    {"name": "mini puff", "flour": 15},
    {"name": "baguette", "flour": 75},
    {"name": "cupcake", "flour": 15},
]

bread2 = [
    {"name": "pancake", "flour": 15},
    {"name": "waffle", "flour": 25},
    {"name": "bagel", "flour": 15},
    {"name": "cupcake", "flour": 15},
    {"name": "choco chips", "flour": 10},
    {"name": "mini puff", "flour": 5},
    {"name": "bread", "flour": 30},
]

print(get_breads(bread1, 100))
print(get_breads(bread2, 75))