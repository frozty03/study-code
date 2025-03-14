def nota(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
    


nota_1 = float(input('Digite a nota da avaliação 1: '))
nota_2 = float(input('Digite a nota da avaliação 2: '))
freq = float(input('Digite a frequência do aluno(%): '))

media = nota(nota_1, nota_2)

print('=====STATUS ACADÊMICO=====')

if media >= 6 and freq >= 75:
    print(f'FREQUÊNCIA: {freq}')
    print(f'NOTA: {media}')
    print(f'STATUS: APROVADO')
elif 4 <= media < 6 and freq >= 75:
    print(f'FREQUÊNCIA: {freq}')
    print(f'NOTA: {media}')
    print(f'STATUS: EXAME')
elif media < 4:
    print(f'FREQUÊNCIA: {freq}')
    print(f'NOTA: {media}')
    print(f'STATUS: REPROVADO')
elif freq < 75:
    print(f'FREQUÊNCIA: {freq}')
    print(f'NOTA: {media}')
    print(f'STATUS: REPROVADO')