import numpy as np


mapa = np.random.randint(0, 5, size=(5,5))


while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_coluna, tesouro_linha) != (0, 0):
        break

posicao_jogador = (0, 0)
pontuacao = 0

def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador = mapa.copy()
    linha, coluna = posicao_jogador
    mapa_com_jogador[linha, coluna] = -1

    print('\nMapa Atual:')

    for linha in mapa_com_jogador:
        print(' '.join(map(str, linha)))


while True:
    mostrar_mapa(mapa, posicao_jogador)

    direcao = input('Faça sua jogada: ').strip().lower()

    jogadas = {
        'w': (-1, 0),
        's': (1, 0),
        'd': (0, 1),
        'a': (0, -1)
    }

    if direcao in jogadas:
        nova_posicao = (
            posicao_jogador[0] + jogadas[direcao][0],
            posicao_jogador[1] + jogadas[direcao][1]
        )
    else:
        print('Direção inválida')
        continue

    if not (0 <= nova_posicao[0] < mapa.shape[0] and 
            0 <= nova_posicao[1] < mapa.shape[1]):
        print('Movimento fora do limite')
        continue

    posicao_jogador = nova_posicao
    pontuacao += 1

    if posicao_jogador == (tesouro_linha, tesouro_coluna):
        mostrar_mapa(mapa, posicao_jogador)
        print('\n---------------Parabéns Você ganhou--------------')
        print(f'Pontuação: {pontuacao}')
        print(f'O tesouro estava na posição: {(tesouro_linha, tesouro_coluna)}')
        break



