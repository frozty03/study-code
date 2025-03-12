def celsius_fahrenheit(temp):
    return (temp * 9/5) + 32

def celsius_kelvin(temp):
    return temp + 273.15

def celsius_reaumur(temp):
    return temp * 4/5

def celsius_rankine(temp):
    return (temp + 273.15) * 9/5

def fahrenheit_celsius(temp):
    return (5 * (temp - 32)) /9

def fahrenheit_kelvin(temp):
    return (temp + 459.67) * 5/9

def fahrenheit_reaumur(temp):
    return (temp - 32) * 4/9

def fahrenheit_rankine(temp):
    return temp + 459.67

def kelvin_celsius(temp):
    return temp - 273.15

def kelvin_fahrenheit(temp):
    return (temp * 9/5) - 459.67

def kelvin_reaumur(temp):
    return (temp - 273.15) * 4/5

def kelvin_rankine(temp):
    return temp * 9/5

def reaumur_celsius(temp):
    return (5 * temp) / 4

def reaumur_fahrenheit(temp):
    return (temp * 9/4) + 32

def reaumur_kelvin(temp):
    return (temp * 5/4) + 273.15

def reaumur_rankine(temp):
    return (temp * 9/4) + 491.67

def rankine_celsius(temp):
    return ((temp - 491.67) / 1.8)

def rankine_fahrenheit(temp):
    return temp - 459.67

def rankine_kelvin(temp):
    return temp * 5/9

def rankine_reaumur(temp):
    return (temp - 491.67) * 4/9

def menu():
    while True:
        print('\n===== MENU DE CONVERSÃO DE TEMPERATURA =====')
        print('1. Celsius para outra escala')
        print('2. Fahrenheit para outra escala')
        print('3. Kelvin para outra escala')
        print('4. Réaumur para outra escala')
        print('5. Rankine para outra escala')
        print('6. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao in ['1', '2', '3', '4', '5']:
            temp = float(input('Digite a temperatura: '))

            if opcao == '1':
                print(f'{temp} celsius = {celsius_fahrenheit(temp)} fahrenheit')
                print(f'{temp} celsius = {celsius_kelvin(temp)} kelvin')
                print(f'{temp} celsius = {celsius_reaumur(temp)} réaumur')
                print(f'{temp} celsius = {celsius_rankine(temp)} rankine')

            elif opcao == '2':
                print(f'{temp} Fahrenheit = {fahrenheit_celsius(temp)} Celsius')
                print(f'{temp} Fahrenheit = {fahrenheit_kelvin(temp)} Kelvin')
                print(f'{temp} Fahrenheit = {fahrenheit_reaumur(temp)} Réaumur')
                print(f'{temp} Fahrenheit = {fahrenheit_rankine(temp)} Rankine')

            elif opcao == '3':
                print(f'{temp} Kelvin = {kelvin_celsius(temp)} Celsius')
                print(f'{temp} Kelvin = {kelvin_fahrenheit(temp)} Fahrenheit')
                print(f'{temp} Kelvin = {kelvin_reaumur(temp)} Réaumur')
                print(f'{temp} Kelvin = {kelvin_rankine(temp)} Rankine')

            elif opcao == '4':
                print(f'{temp} Réaumur = {reaumur_celsius(temp)} Celsius')
                print(f'{temp} Réaumur = {reaumur_fahrenheit(temp)} Fahrenheit')
                print(f'{temp} Réaumur = {reaumur_kelvin(temp)} Kelvin')
                print(f'{temp} Réaumur = {reaumur_rankine(temp)} Rankine')

            elif opcao == '5':
                print(f'\n{temp} Rankine = {rankine_celsius(temp)} Celsius')
                print(f'{temp} Rankine = {rankine_fahrenheit(temp)} Fahrenheit')
                print(f'{temp} Rankine = {rankine_kelvin(temp)} Kelvin')
                print(f'{temp} Rankine = {rankine_reaumur(temp)} Réaumur')

        elif opcao == '6':
            break
        else:
            print('Opção inválida!')
        
menu()
