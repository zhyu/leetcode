class Solution:
    # @return an integer

    def romanToInt(self, s):
        res = 0
        table = {
            'M': 1000, 'MC': 900, 'D': 500, 'DC': 400, 'C': 100, 'CX': 90,
            'L': 50, 'LX': 40, 'X': 10, 'XI': 9, 'V': 5, 'VI': 4, 'I': 1
        }
        symbols = [
            'M', 'MC', 'D', 'DC', 'C', 'CX', 'L', 'LX', 'X', 'XI',
            'V', 'VI', 'I'
        ]
        s = s[::-1]
        while s:
            for symbol in symbols:
                if s.endswith(symbol):
                    res += table[symbol]
                    s = s[:-len(symbol)]
                    break
        return res
