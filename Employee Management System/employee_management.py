class Employee:
    def __init__(self, employee_id, name, salary, department):
        self.id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def update_department(self, new_department):
        self.department = new_department

    def display_employee_details(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.salary:.2f}, Department: {self.department}")


class EmployeeDatabase:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        if employee.id in self.employees:
            print("Employee ID already exists.")
        else:
            self.employees[employee.id] = employee
            print("Employee added successfully.")

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            print("Employee removed successfully.")
        else:
            print("Employee ID not found.")

    def update_employee_details(self, employee_id, new_details):
        employee = self.employees.get(employee_id)
        if employee:
            if 'name' in new_details:
                employee.name = new_details['name']
            if 'salary' in new_details:
                employee.salary = new_details['salary']
            if 'department' in new_details:
                employee.department = new_details['department']
            print("Employee details updated successfully.")
        else:
            print("Employee ID not found.")

    def display_all_employees(self):
        if not self.employees:
            print("No employees in the database.")
        else:
            for employee in self.employees.values():
                employee.display_employee_details()

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for employee in self.employees.values():
                    file.write(f"{employee.id},{employee.name},{employee.salary},{employee.department}\n")
            print("Employee records saved successfully.")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    employee_id, name, salary, department = line.strip().split(',')
                    self.employees[employee_id] = Employee(employee_id, name, float(salary), department)
            print("Employee records loaded successfully.")
        except Exception as e:
            print(f"Error loading from file: {e}")


def menu():
    db = EmployeeDatabase()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee Details")
        print("4. Display All Employees")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")
            employee = Employee(employee_id, name, salary, department)
            db.add_employee(employee)

        elif choice == '2':
            employee_id = input("Enter Employee ID to remove: ")
            db.remove_employee(employee_id)

        elif choice == '3':
            employee_id = input("Enter Employee ID to update: ")
            print("Enter new details (leave blank to skip):")
            name = input("New Name: ")
            salary = input("New Salary: ")
            department = input("New Department: ")

            new_details = {}
            if name:
                new_details['name'] = name
            if salary:
                new_details['salary'] = float(salary)
            if department:
                new_details['department'] = department

            db.update_employee_details(employee_id, new_details)

        elif choice == '4':
            db.display_all_employees()

        elif choice == '5':
            filename = input("Enter filename to save records: ")
            db.save_to_file(filename)

        elif choice == '6':
            filename = input("Enter filename to load records: ")
            db.load_from_file(filename)

        elif choice == '7':
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
