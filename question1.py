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
def check(string):
    Stack = stack()
    count = 0
    error = 0
    checkDict = {'(':')', '{':'}', '[':']'}
    for i in string:
        count += 1
        if i in ('(','{','['):
            if Stack.isEmpty():
                error = count
            Stack.push(i)
        elif i in (')','}',']'):
            if checkDict.get(Stack.peak()) == i:
              Stack.pop()
            else:
                break 
    else:
        if Stack.isEmpty():
            return "Success"
        else:
            return error
    if Stack.isEmpty():
        return "Success"
    else:
        return count
string = input()
print(check(string))

