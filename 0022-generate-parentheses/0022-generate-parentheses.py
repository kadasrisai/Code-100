class Solution(object):
    def generateParenthesis(self, n,currentString = '',close = 0):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1 and close == 0:
            return [currentString+"()"]
        elif n == 0 and close == 1:
            return [currentString+")"]

        allPossibleVariations = []  

        if n >= 1:
            getSubVariations = self.generateParenthesis(n-1,currentString+"(",close+1)
            if type(getSubVariations) != str:
                for item in getSubVariations:
                    allPossibleVariations.append(item)
            else: allPossibleVariations.append(getSubVariations)

        if close >= 1:
            getSubVariations = self.generateParenthesis(n,currentString+")",close-1)
            if type(getSubVariations) != str:
                for item in getSubVariations:
                    allPossibleVariations.append(item)
            else: allPossibleVariations.append(getSubVariations)
        return allPossibleVariations
        