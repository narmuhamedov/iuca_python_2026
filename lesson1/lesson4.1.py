import random

player = {
    'name': '',
    'hp': 100,
    'gold': 0,
    'invertory': []
}

events = [
    {'desc': 'Вы нашли заброшенный сундук.', 'type': 'chest', 'gold':50, 'item': "Ржавый меч"},
    {'desc': 'На вас напал дикий кабан', 'type': 'enemy', "damage": 20, 'gold': 30},
    {'desc': 'Вы встретили бродячего торговца', 'type': 'traider', "cost":40, 'item': 'Зелье лечения'},
    {'desc': 'Вы попали в ловушку со змеями', 'type': 'trap', "damage":15},
    {'desc': 'Вы вышли на дорогу можете передохнуть', 'type': 'peace', 'hp_restore':10},
]

print('===ДОБРО ПОЖАЛОВАТЬ В ТЕМИНАЛ ИГРУ===')
player['name'] = input('Введите имя: ')
print(f'\n{player["name"].capitalize()}, у вас есть 10 шагов чтобы выжить и пройти игру!\n')


for step in range(1,11):
    if player['hp'] <=0:
        print('👻Вы погибли от полученного урона...GAME OVER👻')
        break
    print(f'---ШАГ {step}/10---')
    print(f'❤️ Здоровье: {player["hp"]} | 💵 Золото: {player['gold']} | 🧺 Инвентарь: {player["invertory"]}')


    current_event = random.choice(events)
    print(f'\nСобытие: {current_event['desc']}')

    if current_event['type'] == 'chest':
        print('1.Открыть сундук')
        print('2.Пройти мимо')
        choice = input('Ваш выбор?(1/2)')

        if choice == '1':
            player['gold'] += current_event['gold']

            if current_event['item'] not in player['invertory']:
                player['invertory'].append(current_event['item'])
            print(f'🤸‍♀️Вы нашли {current_event["gold"]} золота и предмет {current_event['item']}!')

        else:
            print('Вы решили не рисковать и прошли дальше!')

    elif current_event['type'] == 'enemy':
        print('1.Сражаться - то потеряете HP, но получу золото')
        print('2.Убегать (50% шанс получить урон!)')
        choice = input('Ваш выбор?(1/2)')
        if choice == '1':
            if 'Ржавый меч' in player['invertory']:
                actual_damage = current_event['damage'] // 2
                print("📏 Благодаря мечу вы получили на 50% урона ниже")
            else:
                actual_damage = current_event['damage']

            player['hp'] -= actual_damage
            player['gold'] += current_event['gold']
            print(f'📏 - Вы победили дикого кабана! Потеряно HP: {actual_damage}, получено золота: {current_event["gold"]}')
        else:
            if random.random()<0.5:
                damage = current_event['damage'] // 2
                player['hp'] -= damage
                print(f'🏃 вы попытались убежать, но кабан укусил вас на прощание!')
            else:
                print(f'🏃 вы убежали без единой царапины!')

    elif current_event['type'] == 'traider':
        print(f'1, Купить {current_event["item"]} за {current_event['cost']} золото')
        print(f'2, Пройти мимо')
        choice = input('Ваш выбор? (1,2): ')
        if choice == '1':
            if player['gold'] >= current_event['cost']:
                player['gold']-= current_event['cost']
                player['invertory'].append(current_event['item'])
                print(f'🧪 Вы купили  {current_event['item']}')
            else:
                print('❌У вас не достаточно золота!')
        else:
            print('Вы попрощались с торговцем! и он пожелал удачной охоты!')

    elif current_event['type'] == 'trap':
        player['hp'] -=current_event['damage']
        print(f'💥 вы получили {current_event["damage"]} Урона от ловушки')


    elif current_event['type'] == 'peace':
        if 'Зелье лечения' in player['invertory']:
            print('У вас есть аптечка, хотите использовать?')
            print('1 - да (100%)')
            print('2 - нет (+10%) ')
            choice = input('Ваш выбор? (1,2): ')

            if choice == '1':
                player['hp']==100
                player['invertory'].remove('Зелье лечения')
                print('🧪 Вы восстановили полностью свое здоровье!')
                continue
        player['hp'] = min(100, player['hp'] + current_event['hp_restore'])
        print(f'🏕️вы отлично отдохнули у костра и восстановили силы {current_event['hp_restore']} HP')


if player['hp'] <=0:
    print('\n👻 GAME OVER')
else:
    print('\n🎉 YOU WIN!!!')
    print(f'Финальный счет - Золото: {player["gold"]} | Здоровье{player["hp"]}')
            
    

        

