class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        zip_strs = zip(*strs)

        for i, letter_group in enumerate(zip_strs):
            if len(set(letter_group)) > 1:
                return strs[0][:i] # return as there are letter not equal
            
        return min(strs) # return as all letters are equal