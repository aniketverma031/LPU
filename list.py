# a = [1, 3, 2, 5, 7, 4]
# for i in range(len(a)):
#     if a[i] == 5:
#         a[i] = 10
# print(a,id(a))



# a = {10,20,40,"a"}
# print(a)
# for i in a:
#     print(i)



# d = {}
# stu = {101:"Rahul",102:"Ajay"}

# print(stu)
# print(stu[101])
# print(stu[102])
# print(stu.values())







# 1 create, display , raise sal , exit 
# enter the name 
# enter the age
# enter the dsignation,programmer25 \, tester20,manager30(y/n) no duplicates store the data
# thank you for using the application

class Employee:
    salary_by_designation = {
        'Programmer': 25000,
        'Tester': 20000,
        'Manager': 30000
    }

    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = Employee.salary_by_designation[designation]

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Designation: {self.designation}, Salary: {self.salary}"

    def raise_salary(self, amount):
        self.salary += amount


# Store employees using a dictionary to avoid duplicates
employees = {}

def create_employee():
    name = input("Enter employee name: ").strip()
    if name in employees:
        print("Employee already exists!")
        return

    try:
        age = int(input("Enter employee age: ").strip())
    except ValueError:
        print("Invalid age input.")
        return

    print("Designations: Programmer, Tester, Manager")
    designation = input("Enter designation: ").strip().capitalize()

    if designation not in Employee.salary_by_designation:
        print("Invalid designation.")
        return

    employee = Employee(name, age, designation)
    employees[name] = employee
    print("Employee added successfully.")

def display_employees():
    if not employees:
        print("No employees to display.")
    else:
        print("\nEmployee List:")
        for emp in employees.values():
            print(emp)

def raise_salary():
    name = input("Enter the name of the employee whose salary you want to raise: ").strip()
    if name not in employees:
        print("Employee not found.")
        return

    try:
        amount = int(input("Enter amount to raise salary: ").strip())
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    employees[name].raise_salary(amount)
    print(f"Salary raised for {name}. New salary: {employees[name].salary}")

def main():
    while True:
        print("\nMenu:")
        print("1. Create Employee")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            create_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            raise_salary()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

        cont = input("Do you want to continue? (Y/N): ").strip().lower()
        if cont != 'y':
            print("Thank you for using Employee Management System.")
            break

if __name__ == "__main__":
    main()
