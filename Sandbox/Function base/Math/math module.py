import math
import random

strlist = ["s","t","r"]
numlist = [1,2,3,4,5,6,7,8]

#выбор случайного элемента списка/кортежа
print(random.choice(strlist))
print()
#перемешивание списка
random.shuffle(numlist)
print(numlist)
print()

#sample(<Лоследовательность>, <Количество элементов>)-
# список из указанного количества элементов.
print(random.sample("abcdefg",2))
print(random.sample(numlist,2))
print(random.sample(range(300),5))

# Пример: генератор пароля

def password_generator(count_char=8):
    arr = ['a','b','c','d','e','f','1','2','3','4','5','6','7','8','9',
           '0']
    passw = []
    for i in range(count_char):
        passw.append(random.choice(arr))
    return "".join(passw)

print(password_generator(4))
print()