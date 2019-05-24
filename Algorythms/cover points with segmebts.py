n = int(input())
l = []
r = []
inp = []
r_l = []
for i in range(0, n):
    inp.append(input().split(' ', n*2))
for i in range(0, n):
    l = (int(inp[i][0]))
    r = (int(inp[i][1]))
    r_l.append([r, l])
    #l[i] = (int(inp[i][0]))
    #r[i] = (int(inp[i][1]))
print(r_l)

r_l.sort()
"""
отсортировали по правому концу - сначала самые "левые", 
потом направо по числовой оси
"""
print(r_l)
coord=[]
coord.append(r_l[0][0])
cnt=1
for i in range(0,n):
    if r_l[i][1] > coord[(len(coord)-1)]:
        """
        если левая(вторая) коорд-та i-го отрезка больше правой координаты предыдущего, то
        увеличить счетчик и добавить отрезок в список
        """
        cnt=cnt+1
        coord.append(r_l[i][0])

print(cnt)
print(" ".join(str(i) for i in coord))