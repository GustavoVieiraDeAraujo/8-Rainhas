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

def pega_as_posicoes_das_rainhas(tabuleiro):
    '''
    Esta função recebe uma matriz que representa um tabuleiro de xadrez.
    A função percorre essa matriz salvando a posição das rainhas, as quais
    são representadas pelo algorismo 1, e retorna uma lista com as posições.
    '''
    lista_das_posicoes = []
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] == 1:
                lista_das_posicoes.append([i, j])
    return lista_das_posicoes
