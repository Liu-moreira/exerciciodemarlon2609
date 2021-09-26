# Faça um programa que leia um nome de usuário e a sua senha e 
# não aceite a senha igual ao nome do usuário, mostrando uma 
# mensagem de erro e voltando a pedir as informações.

nome = str(input('Digite o usuário: '))
senha = str(input('Digite a senha: '))
if senha == nome:
    print('A senha tem que ser diferente do usuário! ')
    print(str(input('Digite a senha: ')))
