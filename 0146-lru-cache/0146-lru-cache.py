class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.memory={}
        self.stack=[]
        self.capacity=capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if key is present in the memory
        if key in self.memory:
            # update LRU stack
            self.updateStack(key)
            # return the value
            return self.memory[key]
        # else return -1
        return -1

    def updateStack(self,key):
        # if key is already present in the stack
        if key in self.stack:
            # get it's current index and remove it
            curIndex=self.stack.index(key)
            self.stack.pop(curIndex)
        # add the key in to the LRU stack    
        self.stack.append(key)    
            
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if the memory is full and the key is not present
        if len(self.memory)==self.capacity and (key not in self.memory):
            # remove the least used item from stack and memory
            lastKey=self.stack.pop(0)
            self.memory.pop(lastKey)
        # add/update the key in stack and memory     
        self.memory[key]=value
        self.updateStack(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)