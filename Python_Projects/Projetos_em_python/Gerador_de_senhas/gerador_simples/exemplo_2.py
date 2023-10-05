
import random

min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
sybs = '[]{}()@#%;/*-_'

qnt = input('Digite o tamanho da senha: ')
qntInt = int(qnt)
length = qntInt
'''
# Fazendo senha com todos
all =  min + max + num + sybs
passwordAll = ''.join(random.sample(all,length))

print('passwordAll = ' + passwordAll)


# Só maiúsculas e números
MAXnum = max + num
passwordMAXnum = ''.join(random.sample(MAXnum,length))

print('passwordMAXnum = ' + passwordMAXnum)
'''

# Só minusculas e maiúculas
MAXmin = max + min
passwordMAXmin = ''.join(random.sample(MAXmin,length))

print('passwordMAXmin = ' + passwordMAXmin)


