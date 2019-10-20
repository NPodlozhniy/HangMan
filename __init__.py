class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class One_linked_list:
    def __init__(self):
        self.first = None
        self.middle = None
        self.last = None
        self.mod_2 = 0

    def clear(self):
        self.__init__()
        
# указатель middle всегда лежит на центральном элементе при нечетном их кол-ве, и на более раннем при четном
    def push(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.middle = self.first
            self.last = self.first
        else:
            self.last.next = Node(x, None)
            self.last = self.last.next
            if self.mod_2 % 2 == 0:
                self.middle = self.middle.next
        self.mod_2 += 1

    def pop(self):
        if self.first == None:
            return None
        elif self.first == self.last:
            val = self.first.value
            self.first = self.first.next
            self.middle = self.first
            self.last = self.first
        else:
            val = self.first.value
            self.first = self.first.next
            if self.mod_2 % 2 == 0:
                self.middle = self.middle.next
        self.mod_2 -= 1
        return val
    
    def size(self):
        length = 0
        if self.first != None:
            current = self.first
            while current.next != None:
                current = current.next
                length += 1
        return length + 1
    
    def push_vip(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.middle = self.first
            self.last = self.first
        else:
            self.middle.next = Node(x, self.middle.next)
            if self.mod_2 == 1:
                self.last = self.last.next
            if self.mod_2 % 2 == 0:
                self.middle = self.middle.next
        self.mod_2 += 1
        
goblins_que = One_linked_list() 
N = int(input()) 
out_arr = []

for i in range(N):

    input_pair = input().split() 

    if input_pair[0] == '+': 
        goblins_que.push(input_pair[1]) 

    elif input_pair[0] == '*': 
        goblins_que.push_vip(input_pair[1]) 

    else: 
        out_arr.append(goblins_que.pop()) 

for num in out_arr: 
    print(num)