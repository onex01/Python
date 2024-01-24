print("Hello, World!")
print(5**5)

# в print() для показания специальных символов нужно использовать \
print("\"Khal Drogo's favorite word is \"athjahakar\"")

# \n - это <ENTER>
print("Hi!\nO, Hello")

# <print(chr(126))> = ~ т.е. 126 имея двоичную запись имеет какой либо символ
print(chr(126))

# можно задать перемну с любым значение, текст ли это, или же просто цифра, переменная задаётся любым словом или буквой, но не цифрой
test = 'test переменной'
print(test)

# можно добавить <+> иногда полезная штука
a = 'Hello, '
b = 'World!'
print(a+b)

# при помощи + можно добавлять не только переменные, но к этим переменным добавлять свои значение
aa = 'Hello'
bb = 'World'
print(aa+", "+bb+"!")

# print(...(str(...+|-|*|/|**|...) складывает переменные в print
# practik begin
king = "Rooms in King Balon's Castle:"
castle = 6
rooms = 17
print(king+"\n"+(str(castle*rooms)))
# practik end

# константа, это обычная переменная, но принято их записывать с большой букву
MY_FRAIND = 15

# Буква f указывает на то, что мы создаем f-строку — шаблон, в который с помощью фигурных скобок подставляются значения переменных. На выходе получается обычная строка.
first_name = 'Joffrey'
greeting = 'Hello'
print(f'{greeting}, {first_name}!')

# tape = ...
# print(tape[0]) => выводит определенную букву
name = 'Ilya'
print(name[0]+name[1]+name[2]+name[3])
# отрицательный индекс print(tape[-1]) начинает выдавать символы с конца
print(name[-1]+name[-2]+name[-3]+name[-4])
mid = name[1:3]
print(mid)
print(name[1:3])

# заместо \n можно испльзовать """ или '''
text = """Это работает очнеь просто
например
вот так"""
print(text)

# int() это функция, которая приобразует информацию
int_test = int('5')
print(int_test)
int_test1 = int(False)
int_test2 = int(True)
print(int_test1)
print(int_test2)
int_test3 = int('3') # если задать значение 3.5 и тд, то он либо не будет работать, либо уберет дробную часть
print(int_test3)
int_test4 = float(5) # преобразует числа с плавающей точкой
print(int_test4)

value = 2.9
print(str(int(value))+' times')

# новая функиция len(), считает количество символов в строке
len_test = len('Hello, World!')
print(len_test)
# еще одна функция pow(), возводит в степень
pow_test = pow(2, 6)
print(pow_test)
# ...
company1 = 'Apple'
company2 = 'Samsung'
com1 = len(company1)
com2 = len(company2)
print(com1 + com2)
# pow(x, y[, z]) Возвращает x в степени y; если z присутствует, возвращает x в степени y, по модулю z

# hex() Преобразовывает число в шестнадцатеричную строку
hex_t = 255
print(hex(hex_t))

# round() функция округляющая до целого числа
round_t = round(99.9)
print(round_t)
round_t1 = round(99.1)
print(round_t1)
# можно задать до какого значения округлять
round_t2 = round(99.25, 1)
print(round_t2)

# повторение, справка
text = 'Never forget what you are, for surely the world will not'
print('First: ' + str(text[0]) +'\n'+ 'Last: ' + str(text[-1]))

# max() переменная которая находит максимальное значение
max_t = max(1, 2, 5, 10 ,25)
print(max_t)
# аналогично и min()
min_t = min(1, 2, 5, 10, 25)
print(min_t)

# Функция random() возвращает случайное число от 0 до 1 с большим количеством знаков после запятой
from random import random
print(round(random() * 10))

# Функция type() позволяет определить тип передаваемого аргумента. Название типа возвращается в виде строки. Например, вызов type(10) вернёт строку <class 'int'>
motto = 'Family, Duty, Honor'
print(type(motto))

name_s = 'Hexlet'
# Метод upper()
upper_name_s = name_s.upper()
print(upper_name_s)  # => 'HEXLET'
# ...
# Переводит в нижний регистр
name.lower()  # 'python'

# print(___.strip()) убирает лишние пробелы
first_name = '  Grigor   \n'
print(first_name.strip())

# ___.find(..) дает индекс символа в переменной
text = 'Never forget what you are, for surely the world will not'
ind1 = text.find('N')
ind2 = text.find(',')
print("Index Of N: " + str(ind1) + "\n" + "Index Of ,: " + str(ind2))

# def дает возможность давать одной функции множество команд, так же они могут быть использованы если они false или true
def print_motto():
    text = 'Winter is coming'
    print(text)
print(print_motto)

# return - это команда похожая на print, но она возвращет число, переменную, функицию и т.д. в начальное пложение, если такое есть
def truncate(text, lenght):
    string = f'{text[:lenght]}...'
    return string

# так же можно в эту функцию добовлять учловия
def word_multiply(text:str, rep:int=1)->str:
    return f'{text * rep}'
print(word_multiply('python', 3))

# тут можно наблюдать, что в функицю is_pensioner было добавлено условие, которое могло давать ответ False и True
def is_pensioner(age):
    if age>=60:
        return True
    else:
        return False

...
