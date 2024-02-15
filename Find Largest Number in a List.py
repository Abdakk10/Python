numbers = [float(input("Enter value {}: ".format(i + 1))) for i in range(10)]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)
