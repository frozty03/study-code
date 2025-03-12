a = int(input('Digite o comprimento do lado A do triângulo: '))
b = int(input('Digite o comprimento do lado B do triângulo: '))
c = int(input('Digite o comprimento do lado C do triângulo: '))

if a == b == c:
    print('É um triângulo equilátero, possio três lados iguais!')
elif a == b or a == c or b == c:
    print('É um triângulo isóscele, possui dois lados iguais!')
else:
    print('É um triângulo escaleno, possui os três lados diferentes!')