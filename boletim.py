def media(nota1, nota2):
    mediapond = (nota1 + nota2 * 2) / 3
    return mediapond

nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))

mediapond = media(nota1, nota2)

if mediapond < 5:
    print('REPROVADO')
elif 8<= mediapond < 9:
    print('PARABÉNS O DESEMPENHO FOI MUITO BOM') 
elif mediapond >= 9:
    print('PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR')
else:
    print('APROVADO')