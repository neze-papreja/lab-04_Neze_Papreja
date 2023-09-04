class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


def sort_employee_data(employee_list, sort_key):
    if sort_key == 1:
        return sorted(employee_list, key=lambda emp: emp.age)
    elif sort_key == 2:
        return sorted(employee_list, key=lambda emp: emp.name)
    elif sort_key == 3:
        return sorted(employee_list, key=lambda emp: emp.salary)
    else:
        return employee_list


def main():
    employee_data = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = int(input("Enter your choice (1/2/3): "))

    sorted_data = sort_employee_data(employee_data, choice)

    print("\nSorted Employee Data:")
    for emp in sorted_data:
        print(emp)


if __name__ == "__main__":
    main()
