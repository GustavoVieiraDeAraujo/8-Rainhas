"""
Funções de teste das funções de implementação do caso da 8 rainhas.
"""

from oito_rainhas import posiciona_rainhas_no_tabuleiro

def testa_montagem_tabuleiro_corretamente():
    '''
    Esta função testa se a função posiciona_rainhas_no_tabuleiro
    esta montando o tabuleiro corretamente com base na entrada passada.
    '''

    entrada = "00001000 01000000 00010000 00000010 00100000 00000001 00000100 10000000"
    saida_esperada = [[0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 1, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0]]

    assert posiciona_rainhas_no_tabuleiro(entrada) == saida_esperada
