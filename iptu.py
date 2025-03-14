def idade_imovel(ano_construção, ano_atual):
    return ano_atual - ano_construção


ano_construção = int(input('Digite o ano de construção do imóvel: '))
ano_atual = int(input('Digite o ano atual: '))

idade = idade_imovel(ano_construção, ano_atual)

if 5 <= idade <20:
    print(f'O móvel tem {idade} anos e possui 15% de desconto no IPTU.')
elif 20 <= idade < 40:
    print(f'O móvel tem {idade} anos e possui 25% de desconto no IPTU.')
elif idade >=40:
    print(f'O móvel tem {idade} anos e possui 30% de desconto no IPTU.')
else:
    print(f'O móvel tem {idade} anos e não possui desconto no IPTU.')
