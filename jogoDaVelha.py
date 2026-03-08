import numpy as np

def colocar_peca (tabuleiro, linha, coluna, peca):
    tabuleiro[linha][coluna] = peca

def verifica_vitoria(tabuleiro, peca):
    linha = np.any(np.all(tabuleiro == peca, axis=1))
    coluna = np.any(np.all(tabuleiro == peca, axis=0))
    diag1 = np.all(np.diag(np.fliplr(tabuleiro == peca)))
    diag2 = np.all(np.diag(tabuleiro == peca))

    return linha or coluna or diag1 or diag2

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | '.join(str(x) if x != 0 else ' ' for x in linha))
        print('-'*9)



tabuleiro = np.zeros((3, 3), dtype=int)

peca_atual = 1
vencedor = False
empate = False

while not vencedor and not empate:
    imprimir_tabuleiro(tabuleiro)

    while True:
        try:
            linha = int(input(f'Faça sua jogada, escolha a linha, jogador {peca_atual}: '))
            coluna = int(input(f'Faça sua jogada, escolha a coluna, jogador: '))
            
            if(linha not in [0, 1, 2] or coluna not in [0, 1, 2]):
                print('escolha uma entrada válida')
                continue
            if (tabuleiro[linha][coluna] != 0):
                print('Posição ocupada')
                continue

            colocar_peca(tabuleiro, linha, coluna, peca_atual)
            imprimir_tabuleiro(tabuleiro)

            vencedor = verifica_vitoria(tabuleiro, peca_atual)

            if (vencedor):
                break


            if (np.all(tabuleiro != 0)):
                empate = True
                break

            
            peca_atual = 2 if peca_atual == 1 else 1

        except ValueError:
            print('Entrada inválida')
    
    if vencedor:
        print(f'Parabéns jogador {peca_atual}, você ganhou')
        break
    if (empate):
         print('Empate')
         break

