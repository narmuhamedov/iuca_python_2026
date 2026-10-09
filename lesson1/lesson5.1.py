univer = []
techikum = []
army = []
married = []


abiturients = [
    {'name': 'Rasul', 'OPT': 120, 'gender':'male'},
    {'name': 'Amir', 'OPT': 90, 'gender':'male'},
    {'name': 'Arina', 'OPT': 50, 'gender':'female'},
    {'name': 'Alex', 'OPT': 30, 'gender':'male'},
    {'name': 'Masha', 'OPT': 10, 'gender':'female'},
    {'name': 'Malika', 'OPT': 110, 'gender':'female'},
    {'name': 'Laura', 'OPT': 59, 'gender':'female'},
    {'name': 'Elmar', 'OPT': 5, 'gender':'male'},
    {'name': 'Aliia', 'OPT': 120, 'gender':'female'}
]

def all_abit(lst):
    for i in lst:
        for k,v in i.items():
            return(f'{k}-{v}')


all_abit(abiturients)


def selection(lst, univer:list, techikum:list, army:list, married: list):
    for i in lst:
        if i['OPT'] >=110:
            univer.append(i)
       
        elif i['OPT']<=109 and i['OPT']>=60:
            techikum.append(i)
       
        elif i['OPT'] <=59 and i['gender'] == 'male':
            army.append(i)
        
        elif i['OPT'] <=59 and i['gender'] == 'female':
                    married.append(i)

selection(lst=abiturients, univer=univer, techikum=techikum, army=army, married=married)
print("-"*10)
print(f'Универ - {univer}')
print("-"*10)
print(f'Техникум - {techikum}')
print("-"*10)
print(f'Армия - {army}')
print("-"*10)
print(f'Замуж - {married}')