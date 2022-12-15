# LUCAS HOLANDA CAPOANI
# TAREFA 2 - PROGRAMAÇÃO ORIENTADA A OBJETOS

class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao  # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATACANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False  # ou True

    def getNumero(self):
        return f'{self.__numero}'

    def getNomeJogador(self):
        return f'{self.__nome_jogador}'

    def getPosicao(self):
        return f'{self.__posicao}'

    def getSituacao(self):
        return f'{self.__situacao}'

    def getParticipouPartida(self):
        return f'{self.__participou_partida}'

    def setParticipouPartida(self, novoValor):
        self.__participou_partida = novoValor

    def setSituacao(self, novoValor):
        self.__situacao = novoValor


def encontrarJogador(lista, numeroJogador):
    for jogador in lista:
        if jogador.getNumero() == numeroJogador:
            return jogador

lst_jogadores = []
lst_escalados = []
lst_reserva = []
lst_jogadores_substituidos = []

# =================================================================================================================
# OPÇÃO 1: Ler de um arquivo texto todos os jogadores escalados para a copa e armazenar em uma lista (lst_jogadores)
# Cada Elemento da lista será uma instância da classe Jogador.
def lerArquivo():
    with open("convocados.txt", "r", ) as arquivo:
        jogadoresConvocados = arquivo.read().split("\n")
        print("====== CONVOCAÇÃO DA SELEÇÃO BRASILEIRA =======")
        for jogadorConvocado in jogadoresConvocados:
            infoJogador = jogadorConvocado.split(":")
            convocado = Jogador(infoJogador[1], infoJogador[0], infoJogador[2])
            lst_jogadores.append(convocado)
            print(f'{infoJogador[0]} - {infoJogador[1]} - {infoJogador[2]}')

# =================================================================================================================
# OPÇÃO 2: Você deverá escalar 11 dos jogadores para iniciar a partida. Os Jogadores escalados para a partida ficam
# em uma lista (lst_escalados). Alterar o atributo 'participou_partida' para True. Os jogadores que não forem escalados para
# iniciar a partida ficam em uma outra lista (lst_reserva)

def escalarGoleiro():
    escalado = False
    while escalado == False:
        print("""\n====== GOLEIROS CONVOCADOS ====== """)
        for pos, jogador in enumerate(lst_jogadores):
            if jogador.getPosicao() == 'GOLEIRO':
                print(f"{jogador.getNumero()}. {jogador.getNomeJogador()} - {jogador.getPosicao()}")


        goleiro = input("\nDIGITE O NÚMERO DO GOLEIRO A SER ESCALADO: ")
        for pos, jogador in enumerate(lst_jogadores):
            if goleiro == jogador.getNumero() and jogador.getPosicao() == 'GOLEIRO':
                lst_escalados.append(jogador)
                jogador.setParticipouPartida(True)
                lst_jogadores[pos] = jogador
                escalado = True
                print(f'\nGOLEIRO - {jogador.getNomeJogador()} - ESCALADO\n')
                break

        if goleiro != jogador.getNumero() and jogador.getPosicao() != 'GOLEIRO':
            print("\n VALOR INVÁLIDO. TENTE NOVAMENTE.")

def escalarLinha():
    print("======= ESCALAR JOGADORES DE LINHA =======")
    for pos, jogador in enumerate(lst_jogadores):
        if jogador.getPosicao() != 'GOLEIRO':
            print(f"{jogador.getNumero()}. {jogador.getNomeJogador()} - {jogador.getPosicao()}")

    while len(lst_escalados) <= 10:
        num = input("\nNÚMERO DO JOGADOR ESCALADO: ")
        verificar = encontrarJogador(lst_escalados, num)
        if verificar != None:
            print(f'O JOGADOR {verificar.getNomeJogador()} JÁ ESTÁ ESCALADO PARA A PARTIDA.')
        else:
            escalado = encontrarJogador(lst_jogadores, num)
            escalado.setParticipouPartida(True)
            lst_escalados.append(escalado)
            print(f'\n{escalado.getPosicao()} - {escalado.getNomeJogador()} - ESCALADO\n')

    for jogador in lst_jogadores:
        jogadorEscalado = encontrarJogador(lst_escalados, jogador.getNumero())
        if jogadorEscalado == None:
            lst_reserva.append(jogador)

    print('======== ESCALAÇÃO DO BRASIL =========')
    for pos, jogador in enumerate(lst_escalados):
        print(f'\n {jogador.getNumero()} - {jogador.getNomeJogador()}')

# =================================================================================================================
# OPÇÃO 3: Você poderá realizar a substituição de um jogador por outro. Quando isso acontecer o jogador vai para
# a lista de Reserva e o outro para a lista Escalados.

def substituirJogador(xlista, numero):
    for pos, jogador in enumerate(xlista):
        if jogador.getNumero() == numero:
            xlista.pop(pos)

def listarJogador(xlista, numero):
    for jogador in lst_jogadores:
        if jogador.getNumero() == numero:
            xlista.append(jogador)
            return jogador

def substituicao():
    substituido = input('\nDIGITE O NÚMERO DO JOGADOR A SER SUBSTITUIDO: ')
    substituto = input('DIGITE O NÚMERO DO RESERVA A ENTRAR EM CAMPO: ')
    substituirJogador(lst_escalados, substituido)
    substituirJogador(lst_reserva, substituto)
    jogadorEntra = listarJogador(lst_escalados, substituto)
    jogadorSai = listarJogador(lst_reserva, substituido)
    lst_jogadores_substituidos.append(jogadorSai)
    print(f'\n======= SUBSTITUIÇÃO REALIZADA ========= \n'
          f'SAI: {jogadorSai.getNomeJogador()} - {jogadorSai.getNumero()} ↓ \n'
          f'ENTRA: {jogadorEntra.getNomeJogador()} - {jogadorEntra.getNumero()} ↑')

# =================================================================================================================
# OPÇÃO 4: Caso haja alguma expulsão, o jogador sai da lista de Escalados e vai para a lista Reserva.

def expulsao():
    expulso = input('DIGITE O NÚMERO DO JOGADOR EXPULSO: ')
    for pos, jogador in enumerate(lst_jogadores):
        if expulso == jogador.getNumero():
            for escalado in lst_escalados:
                if expulso == escalado.getNumero():
                    lst_escalados.remove(jogador)
                    lst_reserva.append(jogador)
                    jogador.setParticipouPartida(True)
                    jogador.setSituacao("EXPULSO")
                    print(f'{jogador.getNomeJogador()} EXPULSO DE CAMPO!')

# =================================================================================================================
# OPÇÃO 5: Mostrar a escalação de todos jogadores que participaram do jogo, inclusive as substituições e expulsões.
#          Salve esses dados em um arquivo (todosjogadores.txt)

def imprimirEscalacao():
    arquivo = open("todosjogadores.txt", "a")
    info = []
    info.append('\n ====== INFORMAÇÕES DA PARTIDA ====== \n')
    info.append('====== ESCALADOS ======\n')
    for jogadorEscalado in lst_escalados:
        info.append(f'{jogadorEscalado.getNumero()} - {jogadorEscalado.getNomeJogador()} \n')
    info.append('====== EXPULSOS ======\n')
    for jogadorExpulso in lst_reserva:
        if jogadorExpulso.getSituacao() == 'EXPULSO':
            info.append(f'{jogadorExpulso.getNumero()} - {jogadorExpulso.getNomeJogador()} \n')
    info.append('====== SUBSTITUIDOS ======\n')
    for jogadorSubstituido in lst_jogadores_substituidos:
        info.append(f'{jogadorSubstituido.getNumero()} - {jogadorSubstituido.getNomeJogador()} \n')

    arquivo.writelines(info)

# =================================================================================================================
# MENU

def menu():
    while True:
        opcao = input("""\n      MENU
    ===========================
    1- Ler arquivo de jogadores
    2- Escalar time
    3- Realizar Substiuição
    4- Expulsão
    5- Imprimir escalação
    ESCOLHA: """)

        if opcao == "1":
            lerArquivo()
        if opcao == "2":
            escalarGoleiro()
            escalarLinha()
        if opcao == "3":
            substituicao()
        if opcao == "4":
            expulsao()
        if opcao == "5":
            imprimirEscalacao()

menu()