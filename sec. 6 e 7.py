from colorama import init, Fore, Back, Style
init()

idade = int(input('Digite sua idade:'))
if 18 <= idade <60:
    print('Você é adulto!')
elif idade >= 60:
    print('Você é idoso!')
else:
    print('Você é criança!') 

#EXERCÍCIO 1
temp = float(input('\nDigite a temperatura em graus Celsius:')) 
if temp < 10:
    print('Muito frio.')
elif temp < 20:
    print('Está fresco.')
else:
    print('Está quente.')

#EXERCÍCIO 2
hora = float(input('\nDigite a hora atual:'))
if hora < 12:
    print('Bom dia!')
elif hora < 18:
    print('Boa tarde!')
else:
    print('Boa noite!')

#EXERCÍCIO 3
valor = float(input('\nDigite o valor do produto:'))            
if 200 >= valor > 100:
    print(F'O valor final é de R${valor * 0.9: .2f}')
elif valor > 200:
    print(f'O valor final é de R${valor * 0.8: .2f}')
else:
    print(f'O valor final é de R${valor * 0.95: .2f}')

#EXERCÍCIO 4
username = 'admin'
password = '12345'
user = input('\nDigite seu usuário:')
passw = input('Digite sua senha:')
if passw == password and user == username:
    print(Fore.GREEN, 'Login OK!', Fore.RESET)
else:
    print(Fore.RED, 'Usuário ou senha incorretos!', Fore.RESET)

#EXERCÍCIO 5
nota = float(input('\nDigite sua nota:'))
if nota >= 9:
    print('Excelente, você tirou A!')
elif nota >= 7:
    print('Bom trabalho, você tirou B!')
elif nota >= 5:
    print('Você passou, mas precisa melhorar. Sua nota é C!')
else:
    print(Fore.RED, 'REPROVADO!', Fore.RESET)          
