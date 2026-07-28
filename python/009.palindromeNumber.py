class Solution(object):
    def isPalindrome(self, x):
        """
        Código feito usando pilhas

        if x < 0:
            return False

        pilha = []
        pilhaP = []

        for numero in str(x):
            num = int(numero)
            pilha.append(num)

        while pilha:
            n = pilha.pop()
            pilhaP.append(n)

        palindromo = int("".join(map(str,pilhaP)))

        return (palindromo == x)
        """

        if x < 0:
            return False

        original = x
        invertido = 0
        
        while x > 0:
            digito = x % 10
            invertido = invertido * 10 + digito
            x = x // 10

        return invertido == original