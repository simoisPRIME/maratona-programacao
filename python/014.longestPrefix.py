class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefixo = ""

        for posicao in range(len(min(strs, key=len))):
            caractere = strs[0][posicao]

            for palavra in strs[1:]:
                if palavra[posicao] != caractere:
                    return prefixo

            prefixo += caractere

        return prefixo