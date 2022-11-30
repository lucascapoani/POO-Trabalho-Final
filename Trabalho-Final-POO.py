"""
Faça um algoritmo que utilize o menu abaixo:

MENU
======
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
Escolha:


Opção 1: Ler de um arquivo texto todos os jogadores
        escalados para a copa e armazenar em uma
        lista (lst_jogadores)
        Cada Elemento da lista será uma instância
            da classe Jogador.

Opção 2: Você deverá escalar 11 dos jogadores para
        iniciar a partida.
        Os Jogadores escalados para a partida ficam
            em uma lista (lst_escalados)
            Alterar o atributo 'participou_partida'
                para True
        Os jogadores que não forem escalados para
            iniciar a partida ficam em uma outra
            lista (lst_reserva)
Opção 3: Você poderá realizar a substituição de um
        jogador por outro.
        Quando isso acontecer o jogador vai para
            a lista de Reserva e o outro para a
            lista Escalados.

Opção 4: Caso haja alguma expulsão, o jogador sai
        da lista de Escalados e vai para a lista
        Reserva.

Opção 5: Mostrar a escalação de todos jogadores que
        participaram do jogo, inclusive as substituições
        e expulsões.
        Salve esses dados em um arquivo (todosjogadores.txt)
"""

lst_jogadores = []
lst_escalados = []
lst_reserva = []


class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False # ou True

def ler_arquivo_convocados():
    try:
        arquivo = open("convocados.txt", "r")
    except:
        print("OPS. Arquivo não encontrado.")
        return

    for linha in arquivo:
        numero, nome, posicao = linha.split(':')
        lst_jogadores.append(linha.replace('\n', ''))
    print(lst_jogadores)
    arquivo.close()

ler_arquivo_convocados()

# while True:
#     escolha = input("""
#             MENU
#             ======
#             1- Ler arquivo de jogadores
#             2- Escalar time
#             3- Realizar Substiuição
#             4- Expulsão
#             5- Imprimir escalação
#             Escolha: """)

