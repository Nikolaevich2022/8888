# # 5. Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# # продукции, а также узнать её состав.
# # Реализуйте кондитерскую.
# # У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# # т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# # граммах).
# # Предложите выбор:
# # 1. Если человек хочет посмотреть описание: название – описание
# # 2. Если человек хочет посмотреть цену: название – цена.
# # 3. Если человек хочет посмотреть количество: название – количество.
# # 4. Всю информацию.
# # 5. Приступить к покупке:
# # С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# # Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# # списке
# # 6. До свидания

shop = {'торт':[7, 2300, 'медовый, без ГМО, вчерашний'], 'пирожное':[4,1800, 'бисквитное, сочное, свежее'],
'маффин':[3,1500, 'нежный, воздушный, возьмите лучше торт'], 'пончик':[2,1700, 'вкусный, ароматный, портит фигуру']}

choice = []
q = 0
w = []
print('', 'Приветствуем Вас в нашем магазине!', '\n', 'Для выбора действия нажмите цифру из списка!')
print('**********************************')
print('', 1, '-посмотреть описание', '\n', 2, '-посмотреть цену', '\n', 3, '-посмотреть количество',
'\n', 4, '-Всю информацию', '\n', 5, '-Приступить к покупке', '\n', 'н - выход')
print('__________________________________')

while choice != 'н' and choice != '5':
    for i in shop:
        choice = input('введите цифру из списка: ')
        print('**********************************')
        if choice == 'н':
            break
        if choice == '1':
            for i in shop:
                print('описание -', i, '-', shop[i][2])
        if choice == '2':
            for i in shop:
                print('стоимость за 100гр. -', i, '-', shop[i][0], 'р.')
        if choice == '3':
            for i in shop:
                print('осталось -', i, '-', shop[i][1], 'гр.')
        if choice == '4':
            for i in shop:
                print('название - цена за 100гр.- всего гр. |', i, '-', shop[i][0], 'руб -', shop[i][1], 'гр.')
        if choice == '5':
            break
        else:
            print('введите нужную цифру!')
            print('', 1, 'посмотреть описание', '\n', 2, 'посмотреть цену', '\n', 3, 'посмотреть количество',
                   '\n', 4, 'Всю информацию', '\n', 5, 'Приступить к покупке', '\n', 'н - выход')
            print('__________________________________')

q = 0
w = []
cake = []

for i in shop:
    if choice == 'н':
        break
    else:
        print(i)

while cake != 'н' and choice != 'н':
    for i in shop:
        print('**********************************')
        cake = input("введите нужный продукт или 'н' для выхода: ")
        if cake == 'н':
            break
        if cake not in shop:
            print('выберите другой продукт!')
            continue
        amount = float(input('количество продукта в гр.: '))
        if cake in shop:
            if shop[cake][1] < amount:
                print('возьмите меньше либо другой продукт!')
                continue
            else:
                shop[cake][1] -= amount
                w = shop[cake][0]
                w *= amount
                w /= 100
                q += w
                print('осталось:', cake, shop[cake][1])
                continue
    print('__________________________________')

for i in shop:
    print('осталось -', i, '-', shop[i][1], 'гр.,')
print('__________________________________')
print('всего купленно на:', q, 'рублей.')
print('Досвиданье')