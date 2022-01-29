# # не знаю на сколько тут правильно, во всяком случае работает. тут все 6 заданий. своих 60% я отработал.

# #             задание №1

a = 0

while a <= 2:
    q = input('введите число из 7 знаков: ')
    w = 0
    e = 1
    r = 0
    t = 0
    try:
        for i in q:
            i = int(i)
            w += i
            if i % 2 == 0:
                r += 1
            else:
                t += 1
    except ValueError:
        print('введена буква')
        a += 1
        continue

    try:
        for i in q[0], q[2], q[5]:
            i = int(i)
            e /= i
    except ZeroDivisionError:
        print('деление на -', 0)
        continue
    finally:
            a += 1

    if r > t:
        print('четных больше:', r)
        print('сумма всех чисел:', w)
    else:
        print('нечетных больше:', t )
        print('частное 1го, 3го и 6го числа:', e)
        print('четные:' , r, 'нечетные:' ,t)


# #                 задание №2
#
# q = input('введите текст: ')
# r = []
# w = 0
# e = 0
# for i in q:
#     print(i)
#     if i in ['e', 'a', 'i', 'o', 'u', 'y']:
#         w += 1
#         r.append(i)
#     elif i == ' ': # непонятно почему отнимая уменьшает количество согласны
#         e -= 0  # а отсутствие блока согласные увеличивает
#     else:
#         e += 1
# print('гласных: ', w, 'согласных: ', e)
#
# if w == e:
#     print('гласные в тексте: ', r)
#
# #               задание №4
#
# import random
# q = int(input('количество чисел: ', ))
# w = input('искомое число: ', )
# e = [random.randint(0, 999) for i in range(q)]
# r = 0
# print(e)
# e = str(e)
#
# for i in e:
#     if w == i:
#         r += 1
# print(r)
#
# #               задание №5
#
# q = input('введите все подряд: ')  # лепим что хотим кроме латиницы и отрицательных чисел
# u = len(q)
# w = []
# e = []
# r = 0
# t = ' '
#
# for i in q:
#     if '0' <= i <= '9':
#         w.append(i)
#         r += 1
#         if r >= 1:
#             e.append(w)
#             continue
#
#     if i.isalpha() and r != 0:
#         w.append(t)
#         r = 0
#         continue
#     else:
#         continue
#
# w = ''.join(str(i) for i in w)
#
# print(w)
#
# #              задание №6

# q = []
# w = []
# r = 0
# t = 0
# # text = 'jkzLMDasdASD'
# text = input('ведите буквы разных регистров:')
# # text = ''.join(str(i) for i in text)
#
# for i in text:
#     if i.islower():
#         q.append(i)
#         if q.index(i) == True:
#             r += 1
#             q.clear()
#             w.clear()
#         else:
#             continue
#     if i.isupper():
#         w.append(i)
#         if w.index(i) == True:
#             t += 1
#             w.clear()
#             q.clear()
#         else:
#             continue
#
# print('количество пар нижнего регистра:', r)
# print('количество пар верхнего регистра:', t)



#
# q = input('введите буквы верхнего и нижнего регистра: ')
# #q = []
# w = 0
# e = 0
# r = []
# t = []
#
#
#    три буквы подряд одного регистра считает как 2е пары!
# for i in range(1, len(q)):  # бежим быстро по строчке
#     if q[i - 1].islower() and q[i].islower():  # пара сравнения нижнего регистра
#         w += 1
#     if q[i - 1].isupper() and q[i].isupper():  # пара сравнения верхнего регистра
#         e += 1
#
# print(r)
# print('пары нижнего регистра:', w)
# print('пары верхнего регистра:', e)
#
#
#q = input('введите все подряд: ')  # лепим что хотим кроме латиницы и отрицательных чисел
# u = len(q)
# w = []
# e = []
# r = 0
# t = ' '
#
# for i in q:
#     #if i == ' ':
#         #w.append(t)
#         #r = 0
#     if '0' <= i <= '9':  #  ищем цифры в формате текст
#         w.append(i)  #  записываем в файл для последующей обработки
#         r += 1  #  счётчик для определения длинны цифры
#         if r >= 1:
#             e.append(w)  #  запись последовательности цифры
#             #continue
#
#     elif i.isalpha() or i == ' ':  #  определение значения и ограничение количества записей
#         if r != 0:
#             w.append(t)  #  при выполнении условия запись раздилителя
#             r = 0  #  обнуление счётчика
#             #continue
#     else:
#         continue
#
# w = ''.join(str(i) for i in w)  #  переводим сисок в строку
#
# print(w)
# #            задание №3
#
# import random
# y = 0
# o = 0
# p = 0
# y == o
# a = []
# s = []
#
# e = 0
# while e <= 5:
#     q = int(input('введите число 1 - 20: '))
#     w = int(input('введите число 1 - 20: '))
#     r = random.randint(1,20)
#     t = random.randint(1,20)
#     if q > r and w > t:  # оба числа больше
#         y += 1
#     else:
#         o += 1
#
#     e += 1  # счетчик вайл
#     p += 1  # счетчик итераций
#     if p == 4:  # запись 4й итерации
#         a.append(q)
#         a.append(w)
#         s.append(r)
#         s.append(t)
#     if y == o and p >= 4:  # чтоб итерация отработала
#         print('загаданное в 4й итерации: вы:', a, 'рандом:', s)
# print('пара больше раз:', y)
# print('остальные случаи:', o)

