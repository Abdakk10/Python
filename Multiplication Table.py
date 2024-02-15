number = int(input("Enter a number for multiplication table: "))

print("Multiplication table for", number)
for i in range(1, 11):
    result = number * i
    print("{} * {} = {}".format(number, i, result))
