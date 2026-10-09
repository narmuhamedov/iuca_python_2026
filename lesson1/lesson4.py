





#dict
# borsh = {'мясо', 'капуста', 'свекла', 'картошка', 'специи', 'лук', 'сметана'}
# lagman = {'мясо', 'лапша', 'специи', 'лук', 'редька', 'джусай'}

# print(lagman.intersection(borsh))

# print(lagman.union(borsh))


# print(lagman.difference(borsh))

# print(lagman.symmetric_difference(borsh))




# nominal = (1,3,5,10,20,50,100,200,500, '1k', '2k', '5k')
# persons = ('nothing', 'nothing','nothing', 'nothing', 'Togolok M.', 'K.Datka', 'T.Satylganov', 'A.Osmonov', 'S.Karalaev', 'J.Balasagyn', 'Burana', 'S.Chokmorov')

# print(type(nominal))
# print(type(persons))

# banknotes = dict(zip(nominal, persons))

# print(banknotes)

# for k,v in banknotes.items():
#     print(f'{k}-{v}')


# auto = dict(brand='Volkswagen', model='GOLF4',color='black')


# #2 в 1

# auto.update(years=2000)

# auto.update(model='polo')

# #delete

# del auto['color']

# print(auto)


# auto2 = auto.copy()




# print(f'Словарь-2-{auto2}')

# print(auto.keys())
# print(auto.values())
# print(auto2.get('brand'))


# for k,v in auto2.items():
#     print(f'{k}-{v}')



# student = {
#     'name': "Radomir",
#     'age': 29,
#     'hobby': 'dance',
#     1997: 'august',
#     'numbers': ['0555123321', '0777123321'],
#     'education': True
# }

# #create
# student['pets'] = '2 sheperd dog'

# #update
# student['name'] = 'Alex'

# #delete
# del student[1997]

# print(student)
# print(student['name'])
# print(student['numbers'][1])

# for key,value in student.items():
#     print(f'{key}-{value}')
