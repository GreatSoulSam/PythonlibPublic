
#1) В столбец
print("string1")
print("string2")

#2)В строку
print("string1", "string2")

#3)В строку с разделителем
print("string1","string2",sep="+")

#4)Без перевода строки
print("string1","string2",end=" ")
print("string3")

#5)Если требуется вставить перевод строки
for n in range(1, 5):
    print (n, end=" ")
print () # Этот принт выдает перевод строки
print("Этo текст на новой строке")

#6)Большой кусок текста - тройные кавычки
#Форматирование сохраняется
print("""String1 String2
String3""")
