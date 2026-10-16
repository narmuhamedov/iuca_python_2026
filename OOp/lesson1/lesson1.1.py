class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f'Имя: {self.name}-Оклад: {self.salary}сом'

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


company_employees = [
    Manager(name='Alex A.', salary=12000, team_size=5),
    Developer(name='Dmitri B.', salary=20000, programming_language='Python'),
    Developer(name='Rustik A.', salary=50000, programming_language='Java'),
    Manager(name='Altynai D.', salary=10000, team_size=10),
    Developer(name='Anna A.', salary=12000, programming_language='Python')
]

print('Список всех сотрудников')
for emp in company_employees:
    print(emp.get_details())

for emp in company_employees:
    bonus = 0

    if isinstance(emp, Manager):
        if emp.team_size >= 10:
            bonus = 20000
        else:
            bonus = 10000
        print(f'Менеджер {emp.name} получает бонус {bonus}сом за управления командой')

    elif isinstance(emp, Developer):
        if emp.programming_language == 'Python':
            bonus = 15000
            print(f'Разработчик {emp.name} работает на {emp.programming_language} получает крутой бонус {bonus} за знание')
        else:
            bonus = 10000
            print(f'Разработчик {emp.name} работает на {emp.programming_language}, получает бонус {bonus}') 
    final_salary = emp.salary + bonus
    print(f'Итоговая выплата {emp.name}: {final_salary}сом\n')