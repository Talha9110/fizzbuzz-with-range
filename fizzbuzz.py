# Fizzbuzz with range (all the value)
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("Fizzbuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz)
