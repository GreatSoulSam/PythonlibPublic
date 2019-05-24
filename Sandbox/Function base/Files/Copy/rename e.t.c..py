#
#
#
#
# Функции для манипулирования файлами

#####################
# Модуль shutil

# copyfile (<Копируемый файл>, <Куда копируем>) - nозволяет скопировать содержимое
# файла в другой файл. Никакие метаданные (наnример, права достуnа) не коnируются.
# Если файл существует, то он будет перезаnисан.
print("copyfile")
import shutil
f = open(r"file.txt","w")
f.close()
shutil.copyfile(r"file.txt",r"file(copy ver).txt")


# сору ( <Konиpyeмыiir файл>, <Куда копируем>) - nозволяет скоnировать файл.
# Коnируются также nрава достуnа. Если файл существует, то он будет nерезаnисан.

print("\n\ncopy")
shutil.copy(r"file.txt", r"file3.txt")


# сору2 (<Коnируемый файл>, <Куда копируем>) - nозволяет скоnировать файл вместе с
# метаданными. Если файл существует, то он будет nерезаnисан.
print("\n\ncopy2")
shutil.copy2(r"file.txt", r"file4.txt")

# move (<Путь к файлу>, <Куда nеремещаем>) - коnирует файл в указанное место, а затем
# удаляет исходный файл. Если файл существует, то он будет nерезаnисан.

print("\n\nmove")
#shutil.move(r"file3.txt",<куда-нибудь>)


#############################################
#Модуль os

import os

#rename (<Старое имя>, <Новое имя>) - nереименовывает файл. Если исходный файл
#отсутствует или новое имя файла уже существует, то в оnерационной системе Windows
#возбуждается исключение WindowsError.

print("\n\nrename")
try:
    os.rename(r"file4.txt","filenumberthree.txt")
except OSError: #WindowsError наследует OSError
    print("unable to rename")
else:
    print("successfully renamed")

# remove (<Путь к файлу>) и unlink(<Пyть к файлу>)- nозволяют удалить файл.
print("\n\nremove, unlink")
try:
    os.remove(r"file4.txt")
    #os.unlink(r"file4.txt")
except OSError: #WindowsError наследует OSError
    print("unable to remove")
else:
    print("successfully removed")

# Функции в модуле os.path

import os.path
print(os.path.exists(r"file3.txt"))

print(os.path.getsize(r"file.txt"))

# и функции, связанные со временем



###########################################################

# Преобразование пути к файлу / каталогу
import os.path

print(os.path.abspath(r"file.txt"))

print(os.path.isabs(r"file4.txt"))

print(os.path.basename(r"C:\Users\Archivist\PycharmProjects\Sandbox"
                       r"\Function base\Files\Copy\file.txt"))

print(os.path.dirname(r"C:\Users\Archivist\PycharmProjects\Sandbox"
                       r"\Function base\Files\Copy\file.txt"))

print(os.path.split(r"C:\Users\Archivist\PycharmProjects\Sandbox"
                       r"\Function base\Files\Copy\file.txt"))

print(os.path.splitdrive(r"C:\Users\Archivist\PycharmProjects\Sandbox"
                       r"\Function base\Files\Copy\file.txt"))

print(os.path.splitext(r"C:\Users\Archivist\PycharmProjects\Sandbox"
                       r"\Function base\Files\Copy\file.txt"))

print(os.path.join(r"C:\Users\Archivist\PycharmProjects\Sandbox","Function base\Files\Copy","file3.txt"))

print(os.path.join(r"C:\\", "book/folder/", "file.txt"))
p = os.path.join(r"C:\\", "book/folder/", "file.txt")
print(os.path.normpath(p))