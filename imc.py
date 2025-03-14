def calculo_imc(peso, altura):
    imc = peso / altura ** 2
    return imc

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura(m): '))

imc = calculo_imc(peso, altura)

if imc < 18.5:
    print(f'O seu imc é de {imc}, classificado como BAIXO PESO.')
elif 18.5 <= imc < 25:
    print(f'O seu imc é de {imc}, classificado como PESO NORMAL.')
elif 25 <= imc < 30:
    print(f'O seu imc é de {imc}, classificado como SOBREPESO.')
else:
    print(f'O seu imc é de {imc}, classificado como OBESIDADE.')
