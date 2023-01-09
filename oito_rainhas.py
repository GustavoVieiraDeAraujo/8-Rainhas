"""
Funções de Implementação do caso das 8 rainhas.
"""

def posiciona_rainhas_no_tabuleiro(entrada):
    '''
    Esta função recebe uma entrada ( string com uma sequencia de zeros
    e uns separados a cada 8 algorismo por um espaço ).A patir dessa
    entrada a função monta uma matriz que representa essa entradae retorna
    ela.
    '''
    tabuleiro = []
    for linha in entrada.split():
        tabuleiro.append([int(elemento) for elemento in linha])
    return tabuleiro