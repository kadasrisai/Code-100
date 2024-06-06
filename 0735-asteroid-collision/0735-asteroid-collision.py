class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for asteroid in asteroids:
            result = asteroid

            while stack and stack[-1] > 0 and result < 0: 
                last = stack.pop()
                if abs(result) == abs(last):
                    result = 0
                elif abs(result) < abs(last): 
                    result = last

            if result != 0: 
                stack.append(result)
            
        return stack
        