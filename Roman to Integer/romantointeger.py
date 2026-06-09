class Solution:
    def romanToInt(self, s: str) -> int:

        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            # ... and so on
        }
        total = 0

        for i in range (len(s)):
            current_val = roman_map[s[i]]  
            if (i + 1 < len(s)):
                
                next_val = roman_map.get(s[i+1])

            else:
                next_val = 0

            if(current_val < next_val):
                total -= current_val
            else:
                total += current_val
        
        return total