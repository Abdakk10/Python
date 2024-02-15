employee_salaries = {}

while True:
    name = input("Enter employee name (type 'no' to exit): ")
    if name.lower() == 'no':
        break
    salary = float(input("Enter salary for {}: ".format(name)))
    employee_salaries[name] = salary

print("Employee Salaries:")
for name, salary in employee_salaries.items():
    print("{}: ${}".format(name, salary))