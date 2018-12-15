class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == '':
            return 0
        
        for i in range(len(haystack)):
            # IndexError: string index out of range, like haystack='aaa', needle='aaaa'
            if i+len(needle)>len(haystack):
                return -1
            
            complete = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    complete = False
                    break
            
            if complete: 
                return i
            
        return -1
                
        