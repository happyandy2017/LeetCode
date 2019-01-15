'''
Valid Parentheses
  Go to Discuss
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s): # Note that an empty string is also considered valid.
        """
        :type s: str
        :rtype: bool
        """
        def is_paired(l, r):
            # return (l=='(' and r==')') or (l=='[' and r==']') or (l=='{' and r=='}')
            return l+r in ['()', '[]', '{}']
            
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else: # char in [')', ']', '}']:
                if len(stack) == 0:
                    return False
                if is_paired(stack[-1], char): # last one is paired with new char
                    stack.pop()
                else:
                    return False # exit if not paired, to improve performance
                    
        return len(stack) == 0