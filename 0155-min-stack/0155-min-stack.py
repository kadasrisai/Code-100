class MinStack(object):

    def __init__(self):
        self.s = []
        
    def push(self, val):
        if len(self.s) > 0:
            lastSmallest = self.s[-1][1]
        else:
            lastSmallest = None
        if lastSmallest == None or lastSmallest > val:
            self.s.append((val,val))
        else:
            self.s.append((val, lastSmallest))

    def pop(self) :
        v = self.s.pop(-1)   

    def top(self):
        return self.s[-1][0]

    def getMin(self):
        return self.s[-1][1]
        
    
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()