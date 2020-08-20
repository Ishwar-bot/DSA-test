class stack:
    def __init__(self):
        self.top = -1
        self.stack = []
    def push(self,data):
        self.top += 1
        self.stack.append(data)
    def __len__(self):
        return self.top + 1
    def pop(self):
        if self.top >=0:
            data = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1
            return data
        else:
            return False
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def peak(self):
        if self.top >=0:
            data = self.stack[self.top]
            return data
        else:
            return False
class maxStack: 
    def __init__(self):
        self.maxStack = stack()
        self.Stack = stack()
    def push(self,data):
        if self.Stack.isEmpty() or self.maxStack.peak() <= data:
            self.maxStack.push(data)
        self.Stack.push(data)
    def pop(self):
        data = self.Stack.pop()
        if self.maxStack.peak() <= data:
            self.maxStack.pop()
        return data
    def max(self):
        return self.maxStack.peak()
    def isEmpty(self):
        return self.Stack.isEmpty()
class queue: #using two stacks
    def __init__(self):
        self.stack1 = maxStack()
        self.stack2 = maxStack()
    def enque(self,data):
        self.stack1.push(data)
    def deque(self):
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    def max(self):
        return max(self.stack1.max(), self.stack2.max())
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
next_arr = iter(arr)
window = queue()
for _ in range(m):
    window.enque(next(next_arr))
print(window.max(), end = " ")
for i in range(n - m):
    window.deque()
    window.enque(next(next_arr))
    if i != (n-m-1):
        print(window.max(), end = " ")
    else:
        print(window.max())