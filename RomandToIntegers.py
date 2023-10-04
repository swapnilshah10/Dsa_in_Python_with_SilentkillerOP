def roman_to_integer(s):
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i in range(len(s)):
        if i > 0 and roman_to_int[s[i]] > roman_to_int[s[i-1]]:
            result += roman_to_int[s[i]] - 2 * roman_to_int[s[i-1]]
        else:
            result += roman_to_int[s[i]]
    
    return result
    
class Solution:
    def romanToDecimal(self, S): 
        return roman_to_integer(S)
        # code here