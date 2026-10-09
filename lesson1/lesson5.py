#функции

#**kwargs

# def menu(**kwargs):
#     return kwargs

# monday = menu(breakfast='яйичница', 
#               lunch='Мампар и лагман', 
#               dinner='Гарнир с котлетой по киевски')

# monday.update(night='телятина на гриле в кисло-сладком соусе и на гарнир картошка фри')


# print(monday)




# *args

# def students(*args):
#     return f'Ты {args}\n Тебе {args}\n Направление {args}'

# students = students(str(input('Как зовут? ')), str(input("Сколько лет? ")), str(input('Твоё направление?')))
# print(students)


#Пример Анкета

# def questionnaire(name, age, gender, hobby):
#     return f'Меня зовут - {name}\nМне {age} лет\nя {gender}\nМое хобби {hobby}'
# questionnaire = questionnaire(name=str(input('Как вас зовут?')), 
#                               age=str(input('Сколько вам лет?')), 
#                               gender=str(input('ваш пол? ')), 
#                               hobby=str(input('Ваше хобби? ')))
# print(questionnaire)




#Аргумент по умолчанию

# def square(a,b=43):
#     return a*b

# square = square()
# print(square)





# name = str(input('Как тебя зовут? '))
# print(f'Привет - {name.capitalize()}')


# name2 = str(input('Как тебя зовут? '))
# print(f'Привет - {name2.capitalize()}')


# name3 = str(input('Как тебя зовут? '))
# print(f'Привет - {name3.capitalize()}')


# def greeting(name):
#     return f'Привет {name}'

# greeting1 = greeting(str(input('Как тебя зовут?')))
# greeting2 = greeting(str(input('Как тебя зовут?')))
# greeting3 = greeting(str(input('Как тебя зовут?')))
# print(greeting1)
# print(greeting2)
# print(greeting3)


# def square(a,b):
#     return a*b

# square = square(12,22)
# print(square)