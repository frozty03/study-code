'''#for para strings
for letra in 'desenvolvedor':
    print(letra)
palavra = 'aipapai'
for letra in palavra:
    print(letra)'

message_sent = True
message_data = 'Mensagem enviada com sucesso'

for sent in range(3):
    if message_sent:
        print(message_data)
        break
    else:
        print('Mensagem não enviada')'
'''
#NESTED LOOPS (loop dentro de loop)
'''for numero1 in range(5):
    print(numero1)
    for numero2 in range(5):
        print(numero2)  # imprime 5 vezes para cada numero1

for numero1 in range(1, 6):
    print(f'produto {numero1}:')
    for numero2 in range(1,6):
        print('item:', numero1, 'características:', numero2) '
'''

'''palavra = 'carniça'
for letra in palavra:
    print(f'{letra} ', end='') # end='' para não pular linha
'''
'''#criando retangulo
for linha in range(5):
    for coluna in range(7):
        print('#', end='')
    print()  # desce linha, para n ficar na mesma, devido ao end=''
'''


'''#While loop é excelente p condições
valor = 100
dia = 0

while valor >= 20:
    dia += 1
    print(f'No dia {dia}, o valor será {valor}')
    valor -= 5
'''
'''#Operador ternário
idade = 18
resultado = 'Voto permitido' if idade >= 16 else 'Voto Negado'
print(resultado)
'''

