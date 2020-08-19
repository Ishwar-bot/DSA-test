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
maxstack = maxStack()
number = int(input())
for _ in range(number):
    query = input()
    queryList = query.split()
    operation = queryList[0]
    if operation == "push":
        maxstack.push(int(queryList[1]))
    elif operation == "pop":
        maxstack.pop()
    elif operation == "max":
        print(maxstack.max())