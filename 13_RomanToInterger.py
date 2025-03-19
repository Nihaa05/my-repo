class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }

        result =0
        n = len(s)

        for i in range(n):
            current_value = roman_to_int[s[i]]
            next_value = roman_to_int[s[i+1]] if i <n-1 else 0

            if current_value < next_value:
                result -= current_value

            else:
                result += current_value
        return result

