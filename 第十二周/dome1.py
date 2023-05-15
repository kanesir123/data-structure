class SQueue:
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0
        
    def is_empty(self):
        return self._num == 0
    
    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]    
   
    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e
    
    def enqueue(self, e):
        if self._num == self._len: 
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e 
        self._num += 1
    
    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i) % old_len]
        self._elems, self._head = new_elems, 0

    def __len__(self):
        return self._num

def cards_game(n):
    # 请补充本函数的定义体
    sq=SQueue()
    for i in range(1,n+1):
        sq.enqueue(i)
    count=1
    while  sq.__len__()!=1:
        while count<1:
            sq.enqueue(sq.dequeue())
            count+=1
        sq.dequeue()
        count-=1
    return sq.dequeue()
            
    
    
    
    
    
    
    
    
    
    
    
    
# 测试
n = 7
print(cards_game(n))
