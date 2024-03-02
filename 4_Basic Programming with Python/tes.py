print("hellow world")

# define function 
def my_function():
    print("Hello from a function")

def my_function_with_args(username,greeting) :
    print("Hello, %s , From My Function!, I wish you %s"% (username,greeting))

# call function
my_function()
my_function_with_args("Sinta", "always happy!")

def sum_two_numbers(a, b):
    return a + b
x = sum_two_numbers(1,2)
print(x)

sentence = "Hello"
for i in range(len(sentence)) :
    print(sentence[i])

for pos, char in enumerate (sentence) :
    print(f"character {char} starts at byte position {pos}")

# def dominant(n int) int {
# var result int = 0
# for i := 0; i < n; i++ {
#    result += 1
#}
#result = result + 10
#return result
#}