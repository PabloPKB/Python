import random
class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim' or resposta == 's':
            self.GerarValorDoDado()
        elif resposta == 'não' or resposta == 'n' or resposta == 'nao':
            print()
            print('Atè mais  =)')
        else:
            print('Digite  apenas sim ou não')
            return simulador.Iniciar()

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))
        return simulador.Iniciar()

simulador = SimuladorDeDado()
simulador.Iniciar()