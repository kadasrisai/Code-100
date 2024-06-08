class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack=[] # maintain the monotonically decresing heights 
        ans=0
        for i in range(0,len(height)):        
            while stack!=[] and height[stack[-1]]<=height[i]: # check if their is any larger height than last smaller height encountered so far in stack
                temp=stack.pop()
                if stack!=[]:
                    h=min(height[stack[-1]],height[i])-height[temp]
                    w=i-stack[-1]-1
                    ans+=h*w
            stack.append(i)
        return ans
        