print('Bem vindo ao AskPython Quiz')
answer = input('Você está pronto para jogar o Quiz? (sim/não): ')
score = 0
total_questions = 3

if answer.lower() == 'sim':
    answer = input('Pergunta 1: Qual sua linguagem de programação favorita? ')
    if answer.lower() == 'python':
        score += 1
        print('Correto')
    else:
        print('Incorreto: ')

    answer = input('Pergunta 2: Você segue algum autor no ASKpython? ')
    if answer.lower() == 'yes':
        score += 1
        print('Correto')
    else:
        print('Incorreto.')

    answer = input('Pergunta 3: Qual é o nome do seu site favorito para aprender Python?')
    if answer.lower() == 'askpython':
        score += 1
        print('Correto')
    else:
        print('Incorreto.')

print(f'Obrigado por jogar esse pequeno Quiz. Você respondeu {score} perguntas corretamente!')
mark = (score / total_questions) * 100
print('Potuação obtida:', mark)
print('BYE!')


