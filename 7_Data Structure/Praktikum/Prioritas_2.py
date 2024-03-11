# No.1
print("NO.1")
def generate_word(word, rooms):
    if len(word) == 0 or rooms == 0:
        return ""
    
    word_length = len(word)
    repetitions = rooms // word_length
    remainder = rooms % word_length
    
    repeated_word = word * repetitions
    partial_word = word[:remainder]
    
    return repeated_word + partial_word

word = input("Masukkan kata : ")
print(generate_word(word, 10))

# No.2
print("\nNO.2")
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_rectangle(height, width, start):
    primes = []
    total = 0
    num = start + 1
    for i in range(height):
        row = []
        for j in range(width):
            while not is_prime(num):
                num += 1
            row.append(num)
            total += num
            num += 1
        primes.append(row)
    return primes, total

def print_prime_rectangle(primes):
    for row in primes:
        print(" ".join(map(str, row)))

bil_prime, total = prime_rectangle(2, 3, 13)
print_prime_rectangle(bil_prime)
print(total)
print("--------------------------------------")
bil_prime, total = prime_rectangle(2, 5, 1)
print_prime_rectangle(bil_prime)
print(total)
