metodo = input('Digite qual método de aferição de temeperatura será convertida em Celsius: ')
temp = float(input('Digite a temperatura: '))

if metodo.lower() == 'fahrenheit':
    C = (5 * (temp - 32)) /9
    print(C)
elif metodo.lower() == 'kelvin':
    C = temp - 273.15
    print(C)
elif metodo.lower() == 'reaumur' or metodo.lower() == 'réaumur':
    C = (5 * temp) / 4
    print(C)
elif metodo.lower() == 'rankine':
    C = ((temp - 491.67) / 1.8)
    print(C)