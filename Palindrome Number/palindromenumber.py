class Solution:
    def isPalindrome(self, x: int) -> bool:
        convertido = str(x)
        
        if (x<0):
            return False
        elif (convertido == convertido[::-1]):
            return True
        else:
            return False

            
