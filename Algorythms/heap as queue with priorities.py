# Первая строка входа содержит число операций 1≤n≤10^5.
# Каждая из последующих n строк задают операцию одного из следующих двух типов:
#
# Insert x, где 0≤x≤109 — целое число;
# ExtractMax.
# Первая операция добавляет число x в очередь с приоритетами,
# вторая — извлекает максимальное число и выводит его.
#
# Крафтим макс-кучу
import math

n = int(input())
q=[0] # ИНициализируем первый элемент нулем, для сохранения нумерации
#print(n)
for i in range(0,n):
    # Считываем команды
    c = input()

    if c.startswith("I"):
        c,p = c.split()
        p = int(p)
        q.append(p) # Добавляем в конец очереди р

        # Сначала расставим деьтей слева направо
       #  for j in range(1, len(q)-1):
        #             while 2*j< len(q)-1:
        #                 if q[2*j]>q[2*j+1]:
        #                     q[2*j],q[2*j+1]=q[2*j+1],q[2*j]
        #                 j+=1

        for j in range(1,len(q)-1):#refactor tree
            if 2*j+1<=len(q)-1:
                if q[j]< max(q[2*j],q[2*j+1]): # Если родитель меньше max сына
                    ind = q.index(max(q[2*j],q[2*j+1]))
                    q[j], q[ind] = q[ind], q[j]# меняем их местами

                    if q[2*j]>q[2*j+1]: # Если левый сын больше правого
                        q[2*j],q[2*j+1]= q[2*j+1],q[2*j] # меняем их местами
            elif 2*j<=len(q)-1 and 2*j+1>len(q)-1:
                if q[j]<q[2*j]:  # Если родитель меньше сына
                    q[j],q[2*j]= q[2 * j],q[j]  # меняем их местами
         
        # if q[math.floor(j/2)] < q[j]: # Если родитель меньше ребенка
           #     q[math.ceil(j/2)],q[j] = q[j],q[math.ceil(j/2)] # Меняем их местами

                # А если детей двое?

        #print(q)
        #if q[math.ceil(q.index(p)/2)]<p and q.index(p)>0: #shiftup
            #q[math.ceil(q.index(p) / 2)], q[q.index(p)]= \
                #q[q.index(p)], q[math.ceil(q.index(p) / 2)]
    elif c.startswith("E"):
        print(q[1])
       # print(q)

        #del(q[-1])
        del(q[1])
#print(q[1:])

# t=q.index(max(q[1:]))
#         q[t]=min(q[1:])-1 # Присваиваем значение меньше самого малого
#         for j in range(1,len(q)-1):
#             alp = q.index(q[-1])
#             bet = 2*j+1
#             if alp < bet and bet <= len(q):
#                 if q[2*j]>q[j]:# or q[2*j+1]>q[j]: #refactor tree #outofrange +1
#                     q[j],q[2*j]=q[2*j],q[j]
#             elif bet< len(q) and alp>=bet:
#                 if q[2 * j] > q[j]  or q[2*j+1]>q[j]:
#                     tmp,ind = max(q[2*j],q[2*j+1]),q.index(max(q[2*j],q[2*j+1]))
#                     q[j],q[ind] = tmp,q[2*j+1]
#
#                 """if len(q)>2*i+1:
#                     q[i]= q[2*i]
#                 else:
#                     q[i]=max(q[2*i+1],q[2*i])"""