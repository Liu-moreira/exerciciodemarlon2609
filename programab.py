# Faça um Programa que verifique se uma letra digitada é "F" ou
#  "M". Conforme a letra escrever: F - Feminino, M - Masculino, 
#  Sexo Inválido.

sexo = str(input('Informe seu sexo - digite F ou M: ').upper ())
if sexo == 'F':
    print('Feminino')
elif sexo == 'M':
    print('Masculino')
else:
    print('Sexo inválido')