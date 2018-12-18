class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """       
        return s[::-1]

    
class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i = 0
        j = len(s)-1
        while i<j:
            r[i], r[j] = r[j], r[i]
            i+=1
            j-=1
        return ''.join(r)
    
class SolutionReverse(object):
    def reverseString(self, s):
        i = len(s) - 1
        result = ''
        while i>=0:
            result += s[i]
            i -= 1
        return result  
    
class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]
    
class SolutionRecursive(object):
    def reverseString(self, s):
        # recursive
        l = len(s)
        if l<2:
            return s
        
        return self.reverseString(s[l//2:])+self.reverseString(s[:l//2])