'''
Decode String
  Go to Discuss
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        if not s:
            return s
        from collections import deque
        stack = deque()
        curN = 0
        curS = ''
        for c in s:
            if c.isdigit():
                curN = curN*10+int(c)
            elif c == '[':
                stack.append(curS)
                stack.append(curN)
                curN = 0
                curS = ''
            elif c == ']':
                num = stack.pop()
                preS = stack.pop()
                curS = preS + curS*num
            else:
                curS += c
        return curS

#     def decodeString2(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """                
#         def compose_string_in_stack(stack):
#             # get string inside '[]'
#             string = ''
#             while stack:
#                 temp = stack.pop()
#                 if temp != '[':
#                     string += temp
#                 else:
#                     string = string[::-1]
#                     break
#             # find k
#             k = ''
#             while stack:
#                 temp = stack[-1]
#                 if temp in '0123456789': # is digit
#                     k += temp
#                     stack.pop()
#                     if not stack:
#                         k = k[::-1]
#                 else:
#                     k = k[::-1]
#                     break
#             # stack.push(k*string)
#             for char in (int(k)*string):
#                 stack.append(char)
            
#         if not s:
#             return s
#         from collections import deque
#         stack = deque()
#         # iterate s
#         for char in s:
#             if char == ']':
#                 compose_string_in_stack(stack)                
#             else:
#                 stack.append(char)
#         # return result when finishing iterating s
#         result = ''
#         while stack:
#             result += stack.popleft()
#         return result
    