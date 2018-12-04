class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 1. convert array to number, [1, 2, 3] -> 123
        num = 0
        for digit in digits:
            num = num*10 + digit
            
        # 2. num + 1, 123+1=124
        num += 1
        
        # 3. num to array, 124 -> [4, 2, 1]
        result = []
        while num != 0:
            # result.append(num % 10)
            result.insert(0, num%10)

            num = num//10
            
        # 4. [4, 2, 1]->[1, 2, 4]
        # result.reverse()
        
        return result