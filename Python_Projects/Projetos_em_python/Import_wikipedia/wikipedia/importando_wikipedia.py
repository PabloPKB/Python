import time
import wikipedia as wiki
while True:
    pergunta1 = str(input('Deseja continuar? \n Sim [s] '
                          'Não [n] \n Resposta: \n'))
    lingua1 = str(input('Escolhe a língua: '))
    lingua = lingua1.lower()
    # Colocar todas as letras maiúculas
    pergunta = pergunta1.lower()
    if pergunta == 's' or pergunta == 'sim':
        wiki.set_lang(lingua)
        palavra = str(input('Digite o artigo que deseja encontrar: '))
        pa = wiki.page(palavra)
        # Mostrar o site
        url = print(pa.url)
        print('Sumário do Artigo')
        # Mostrar o sumário
        p = print(wiki.summary(palavra))
        artigocompleto = str(input(' Deseja mostrar o artigo completo? '
                                   '\nSim[s] '
                                   'Não [n]\n Resposta: '))
        if artigocompleto == 's' or artigocompleto == 'sim':
            # Artigo completo
            artigo = print(pa.content)

    elif pergunta == 'n' or pergunta == 'não' or pergunta == 'não':
        print('Fim do Programa!')
        time.sleep(3)
        quit()
    else:
        print('\nPor Favor carregue  em [s] para Sim '
              'e [n] para Não!\n')
