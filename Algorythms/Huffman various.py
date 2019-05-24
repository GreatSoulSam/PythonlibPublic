
import heapq
from collections import Counter,namedtuple

class Node(namedtuple("Node",["left","right"])):
    def walk(self,code,acc):
        self.left.walk(code,acc+"0")
        self.right.walk(code, acc+"1")

class Leaf(namedtuple("Leaf",["char"])):
    def walk(self,code,acc):
        code[self.char]=acc or "0"  # ноль - для случая одного(одинаковых) символов


def huffman_encode(s):
    h = []
    """
    добавиляем третий элемент, чтобы не доходить в сравнении листов и нод до
    сравнения char и left, т.е. строки и листа
    """
    for ch, freq in Counter(s).items():
        h.append((freq,len(h),Leaf(ch)))
    #h = [(freq, Leaf(ch)) for ch, freq in Counter(s).items()]
    heapq.heapify(h)

    count = len(h)
    while len(h) >1:
        freq1,_count1,left = heapq.heappop(h)
        freq2,_count2,right = heapq.heappop(h)
        heapq.heappush(h,(freq1+freq2,count,Node(left,right)))
        count+=1

    code = {}
    if h: # если очередь не пустая:
        # послевыхода из вайл в очереди будет один элемент,
        [(_freq,_count,root)]= h # приоритет которого нам не важен, а сам элемент - корень дерева
        root.walk(code,"")
    return code
    #Counter(s) # счетчик появления символа в строке
    #code = {}

    #return{ch: ch for ch in s}

def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code),len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch,code[ch]))
    print(encoded)


def test(n_iter=100):
    """
    код для подключения и тестирования программы декодирования,
    проверка совпадения декодкд и исходной строки
    включает "кривые" случаи
    :param n_iter:
    :return:
    """
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0,32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        assert huffman_decode(encoded,code) == s


if __name__ == "__main__":
    main()

