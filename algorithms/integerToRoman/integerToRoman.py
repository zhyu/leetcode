class Solution:
    # @return a string

    def intToRoman(self, num):
        table = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
            'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }
        symbols = [
            'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V',
            'IV', 'I'
        ]
        res = ''
        for symbol in symbols:
            if not num:
                break
            cnt = num / table[symbol]
            num %= table[symbol]
            res += cnt * symbol
        return res
