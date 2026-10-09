people = [('Иван', 23), ("Аня", 50), ('Петя', 10)]
sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)

numbers = [1,2,3,4]
squarted = list(map(lambda x: x**2,numbers))
print(squarted)







# while 1:
#     try:
#         first_number = int(input('первое число?: '))
#         operation = str(input('+ - * /: '))
#         if operation not in ['+', '-', '*', '/']:
#                     print('Вводите специальные символы + - * /')
#                     continue
#         second_number = int(input('второе число?: '))

#     except ValueError:
#         print('Пожалуйста вводите правильные значения!')
#         print('----'*10)
#         continue
#     try:    
#         if operation == '+':
#             print(f'{first_number}+{second_number}={first_number+second_number}')
#         elif operation == '-':
#                 print(f'{first_number}-{second_number}={first_number-second_number}')
#         elif operation == '*':
#                     print(f'{first_number}*{second_number}={first_number*second_number}')
    
#         elif operation == '/':
#                 print(f'{first_number}/{second_number}={first_number/second_number}')
#     except ZeroDivisionError:
#            print('На ноль делить нельзя!')
#            continue
#     exit_ = str(input('Выйти из калькулятора?Да/Нет '))
#     exit_ = exit_.lower()

#     try:
#         if exit_ == 'да':
#             print("Пока!")
#             break
#         elif exit_ == 'нет':
#             print('Продолжаем')
#             print('-----------')
#             continue
#     except Exception:
#           print('неизвестная ошибка!')
#           break
        
        








# try:
#     number = int(input('Введите число'))
#     print(number/0)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except ValueError:
#     print('Вводите только число')
# except Exception as e:
#     print('Неизвестная ошибка')