secreto = 'perfume'
digitadas = []
chances = 3

print('BORA BRINCAR DE "ADIVINHE A PALAVRA". \n'
      'Digite apenas letras minúsculas, uma de cada vez! \n'
      'VOCÊ TERÁ APENAS 3 CHANCES PARA ACERTAR A PALAVRA')
print()

while True:
    if chances <= 0:
        print('Você PERDEU!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh... Isso não vale. Digite apenas uma letra!')
        print()
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULL, a  letra "{letra}" existe na palavra secreta.')

    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print()
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era "{secreto_temporario}".')
        break

    else:
        print(f'PALAVRA SECRETA: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você tem apenas {chances} chances')
    print()