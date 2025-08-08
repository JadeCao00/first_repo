class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    def print_info(self):
        print(f"姓名{self.name} (工号：{self.employee_id}")

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
       super().__init__(name, employee_id)
       self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self,name, employee_id, daily_salary, work_days):
        super().__init__(name, employee_id)
        self.daily_salary = daily_salary
        self.work_days = work_days
        self.monthly_pay = self.calculate_monthly_pay()

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days


Coco = FullTimeEmployee("可可","1087",7000)
Tina = PartTimeEmployee("缇娜", "1098", 220, 15)

Tina.print_info()
print(Tina.calculate_monthly_pay())
print(Coco.calculate_monthly_pay())




