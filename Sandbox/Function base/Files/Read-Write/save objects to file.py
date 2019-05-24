#
#
#
#
# Модуль pickle

#dump ( <Объект>, <Файл> [, <Протокол>] [, fix imports=True] ) - производит
# сериализацию объекта и записывает данные в указанный файл.
# В параметре <Файл> указывается файловый объект,
# открытый на запись в бинарном режиме.

import pickle
f = open(r"file1.txt",'wb')
obj = ["String1",(2,3)]
obj2 = (3,4)
pickle.dump(obj,f)
pickle.dump(obj2,f)
f.close()

#load() -читает данные из файла и преобразует их в объект.

f = open(r"file1.txt",'rb')
obj = pickle.load(f)
obj2 = pickle.load(f)

print(obj,obj2)

