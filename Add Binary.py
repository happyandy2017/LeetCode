class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 1. a (str)->二进制到十进制a_10 (digit)
        #    b->二进制到十进制b_10
        a_10 = self.binary_to_decimal(a)
        b_10 = self.binary_to_decimal(b)
        
        # 2. c_10 = a_10+b_10 （十进制加法运算）(digit)
        c_10 = a_10 + b_10
        
        # 3. c_10（十进制, digit）->c_2(二进制, str)
        c_2 = self.decimal_to_binary(c_10)
        
        return c_2
        
    def binary_to_decimal(self, binary_str):
        result = 0
        for d in binary_str:
            result = result*2 + int(d)
        return result
        
    def decimal_to_binary(self, decimal_digit):
        result = ''
        while decimal_digit != 0:
            result += str(decimal_digit%2)
            decimal_digit = decimal_digit//2
            
        return result[::-1] if result !='' else '0'#要注意输入可能是'0'+'0'的情况