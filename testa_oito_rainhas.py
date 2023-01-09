"""
Funções de teste das funções de implementação do caso da 8 rainhas.
"""

from oito_rainhas import posiciona_rainhas_no_tabuleiro
from oito_rainhas import pega_as_posicoes_das_rainhas
from oito_rainhas import verifica_se_o_tabuleiro_tem_8_rainhas
from oito_rainhas import verifica_se_o_tabalueiro_tem_64_posicoes
from oito_rainhas import verifica_as_diagonais_da_rainha

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

def testa_pega_as_posicoes_das_rainhas_corretamente():
    '''
    Esta função testa se a função pega_as_posicoes_das_rainhas
    esta retornando as posições corretas da rainhas no tabuleiro.
    '''

    entrada = [[0, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0]]
    saida_esperada = [[0, 4], [1, 1], [2, 3], [
        3, 6], [4, 2], [5, 7], [6, 5], [7, 0]]

    assert pega_as_posicoes_das_rainhas(entrada) == saida_esperada

def testa_se_tabuleiro_tem_8_rainhas():
    '''
    Esta função testa se a função verifica_se_o_tabuleiro_tem_8_rainhas
    esta retornando True quando o tabuleiro tem 8 rainhas.
    '''
    entrada = [[0, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0]]
    saida_esperada = True

    assert verifica_se_o_tabuleiro_tem_8_rainhas(entrada) == saida_esperada

def testa_se_tabuleiro_tem_64_posicoes():
    '''
    Esta função testa se a função verifica_se_o_tabalueiro_tem_64_posicoes
    esta retornando True quando o tabuleiro tem 64 posições.
    '''

    entrada = [[0, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0]]
    saida_esperada = True
    assert verifica_se_o_tabalueiro_tem_64_posicoes(entrada) == saida_esperada

def testa_se_as_diagonais_da_rainha_escolhida_nao_tem_outras_rainhas():
    '''
    Esta função testa se a função verifica_as_diagonais_da_rainha
    esta retornando True quando não tem rainhas nas diagonais da posição
    da escolhida.
    '''
    entrada1 = [[0, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0]]
    entrada2 = [2,3]
    saida_esperada = True
    assert verifica_as_diagonais_da_rainha(entrada1, entrada2) == saida_esperada