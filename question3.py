class queue:
    def __init__(self,maxSize = float("inf")):
        self.items = []
        self.size = 0
        self.maxSize = maxSize
    def enque(self,element):
        if self.size < self.maxSize:
            self.items.append(element)
            self.size += 1
    def dequeue(self):
        if not self.isEmpty():
            temp = self.items[0]
            self.items.remove(temp)
            self.size -= 1
            return temp
        else:
            return False
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return False
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    def isFull(self):
        if self.size ==  self.maxSize:
            return True
        else:
            return False
        
bufferSize, number = input().split() #storing bufferSize and number of interations
instructDict = {} #dict that keeps all the instruction where intime as keys and their execution time as values. for more than instances of same in-time, it stores those values in ordered list.
for _ in range(int(number)):
    intime, runtime = input().split()
    intime = int(intime)
    runtime = int(runtime)
    if intime in instructDict:
        instructDict[intime].append(runtime)
    else:
        instructDict[intime] = [runtime]
time = -1
processtime = 0
error = []
buffer = queue(int(bufferSize)) #buffer
idleCount = 0 #keeps idleCount of no processor activity
idleBreakTime = 30 #iterations of no processor activity before stopping the program
while True: #simulating time one milisecond per loop
    time += 1
    if processtime > 0:
        processtime -= 1
    if not buffer.isEmpty():
        idleCount = 0
        if processtime == 0:
            buffer.dequeue() #remove a task from buffer after it's execution
            error = [i - 1 for i in error]
            if 0 in error:
                print(-1)
                for _ in range(error.count(0)):
                    error.remove(0)
    else:
        idleCount += 1
        if idleCount == idleBreakTime:
            break
    inputpackets = instructDict.get(time)    #adding input packets arrived at this time to buffer
    if inputpackets:
        for packet in inputpackets:
            if not buffer.isFull(): 
                buffer.enque(packet)
            else:
                error.append(int(bufferSize))
    if processtime == 0 and not buffer.isEmpty(): #processor has no tasks at hand and buffer is not empty
        processtime = buffer.peek() #assigning new task
        print(time) #printing time when assignment of new task is done
    
        

