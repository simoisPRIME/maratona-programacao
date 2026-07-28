class Solution(object):
    def romanToInt(self, s):

        valores = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}

        total = 0
        valor_anterior = 0

        for n in s[::-1]:
            valor = valores[n]
            if valor < valor_anterior:
                total -= valor
                valor_anterior = valor
            else:
                total += valor
                valor_anterior = valor
        
        return total