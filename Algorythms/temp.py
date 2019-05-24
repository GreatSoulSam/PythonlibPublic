

"""
class Node:
    def __init__(self): # Конструктор
        self.code = ""     # Атрибут экземпляра класса
        self.freq = 0
    def go_right(self):
        self.code+="1"
    def go_left(self):
         self.code+="0"
class Leaf:
    def __init__(self): # Конструктор
        self.freq = 0
        self.x = 10
        self.parent = Node()
"""
out = ""
k, l = map(int,input().split())

sym, cd = [],[]
for i in range(k):
    s, c = input().split()
    s=s[:-1]
    #c = int(c)
    sym.append(s)
    cd.append(c)
#print(sym,cd)

haff=input()

while len(haff)>0:
    for i in range(0,len(cd)):
        if haff.startswith(cd[i]):
            out=out+sym[i]
            haff=haff[len(cd[i]):]
print(out)