print('Analizando nomes!!!')
nome = str(input('Nome Completo: '))
print(f'Nome maiuscúlo: {nome.upper()}')
print(f'Nome minúsculo: {nome.lower()}')
print(f'Numero de letras: {len(nome) - nome.count(" ")}')
n = nome.split()
print(f'N de letras primeiro nome: {len(n[0])}')
