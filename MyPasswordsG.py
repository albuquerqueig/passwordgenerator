# Gerador de senhas aleatórias (nível de segurança maior)

import random

print('Welcome to the Password Generator!')

# Aqui são definidos os possíveis caracteres
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,?0123456789'

# Aqui é solicitada a informação de quantas senhas deseja gerar (retornando em número)
number = input('Amount of passwords generate: ')
number = int(number)

# Aqui é definido a extensão da quandidade de caracteres
length = input('Input your password length: ')
length = int(length)

# Apresentação do resultado
print('\nhere are your passwords:')

# Uso da bibliotega random com as possibilidades de gerar senha.
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)