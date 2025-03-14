print('FUNÇÃO: \nF(x) = (4 * x**2 - 3 * x + 9) / x')
x = float(input('Digite o valor de x, para x diferente de zero: '))

if x != 0:
    y = (4 * x**2 - 3 * x + 9) / x
    print(f'F({x: .0f} ) = {y}')
else:
    print('OPERAÇÃO NÃO EXISTE!')