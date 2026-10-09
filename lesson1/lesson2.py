# Условные операторы и циклы
# for, while
import random

room = 1
coins = 0
while room <= 10:
    print()
    print('Ты вошел в комнату', room)

    event = random.randint(1,3)

    if event == 1:
        print('На тебя напал монстр👹')
        print('Ты убежал!😬')
    elif event == 2:
        print('🤑 ты нашел 10 монет')
        coins += 10
    else:
        print('🙄 комната пустая!')

    room +=1

print()
print('🧭 Ты прошел все комнаты')
print(f"👑 ты собрал монет - {coins}")












# print("===ПРИКЛЮЧЕНИЕ===")
# print('Тебе нужно пройти 10 шагов')

# step = 1

# while step <= 10:
#     print()
#     print('Шаг', step)
#     print('1 - Идти вперед')
#     print('2 - Повернуть направо')
#     print('3 - Повернуть налево')

#     choice = int(input('Твой выбор: '))

#     if choice == 1:
#         print('Ты пошел вперед!')
#     elif choice == 2:
#         print('Ты пошел направо')
#     elif choice == 3:
#         print('Ты пошел налево')
#     else: 
#         print('Такого варианта нету!')
#         continue

#     step += 1

# print()
# print('Поздравляю ты прошел 10 шагов!')









# apples = 10
# bad_box = 0
# good_box = 0

# while apples !=0:
#     get_apple = int(input('Какое яблоко в руке у вас? 1/хор, 2/плох '))
#     if get_apple == 1:
#         apples -=  1
#         good_box  += 1
#         print(f'Хор ябл - {good_box}\nПлохие яблоки-{bad_box}\nЯблоки-{apples}')
#     elif get_apple == 2:
#         apples -= 1
#         bad_box += 1
#         print(f'Хор ябл - {good_box}\nПлохие яблоки-{bad_box}\nЯблоки-{apples}')


# print(f'Кол-во плохих яблок - {bad_box}\nКол-во хороших яблок - {good_box}')









# while 1:
#     print('Расул привет!')



# counter = 1

# for i in range(1,11):
#     if i<=10:
#         counter + 1
#         print(i)



# if elif else 
# Операторы сравнения > <, >= <=, == , !=, and or


# color = str(input('какой горит цвет светофора? '))
# color = color.lower()
# if color == 'зеленый':
#     print('езжай')
# elif color == 'желтый':
#     print('подготовься к движению')
# elif color == 'красный':
#     print('СТОЙ!')
# else:
#     print('сломан светофор')






#Начало: 23 августа Конец: 22 сентября
# day = int(input('введите дату рождения '))
# month = int(input('введите месяц рождения '))

# if day >= 23 and day <=31 and month == 8 or day<=22 and day>=1 and month==9:
#     print('Вы дева!')
# else:
#     print('Вы другого знака зодиака!')


# name = str(input('Как вас зовут? '))
# name = name.capitalize()
# if name == 'Радомир':
#     print('Вы преподаватель')
# elif name == 'Полина':
#     print('Вы преподаватель')
# else:
#     print('Вы не преподаватель')