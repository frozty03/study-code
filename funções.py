#função xargs, não sabe a quantidade, somar vários numeros de
'''def soma(*numeros): #asterisco antes do parametro
    resultados = 0
    for i in numeros:
        resultados += i
    return resultados  #retorna a soma dos numeros


x = soma(1, 2, 7, 10, 11, 12, 13, 14) #permite adicionar os valores sem limite de quantidade
print(x)
'''

#para vários parâmetros, podendo adicionar dps
'''def carro(**peças): #dois asteriscos
    return peças


print(carro(motor='2.4 litros', ar_condicionado='não'))
print(carro(motor='1.6 litros', ar_condicionado='sim', portas='4'))
'''

