class Employee:
    def __init__(self, name, experience, hourly_rate, hours_worked, salary, bonus):
        self.name = name
        self.experience = experience
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        base_salary = self.hourly_rate * self.hours_worked
        self.bonus = base_salary * self.get_bonus_percentage()
        self.salary = base_salary + self.bonus

    def get_bonus_percentage(self):
        if self.experience < 1:
            return 0.01
        elif self.experience < 3:
            return 0.05
        elif self.experience < 5:
            return 0.08
        else:
            return 0.15

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Стаж: {self.experience} лет")
        print(f"Часовая ставка: {self.hourly_rate} рублей")
        print(f"Отработанные часы: {self.hours_worked} часов")
        print(f"Оклад: {self.salary} рублей")
        print(f"Премия: {self.bonus} рублей")

# Создаем список сотрудников
employees = []

# Ввод данных для каждого сотрудника
n = int(input("Введите количество сотрудников: "))
for i in range(n):
    name = input("Введите ФИО сотрудника: ")
    experience = int(input("Введите стаж работы (в годах): "))
    hourly_rate = float(input("Введите часовую заработную плату: "))
    hours_worked = float(input("Введите количество отработанных часов: "))
    salary = 0.0
    bonus = 0.0

    employee = Employee(name, experience, hourly_rate, hours_worked, salary, bonus)
    employee.calculate_salary()
    employees.append(employee)

# Вывод информации о каждом сотруднике
for employee in employees:
    employee.display_info()
    print()
