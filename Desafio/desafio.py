def calcular_troco (valor, saldo):
    troco = valor - saldo
    return troco
i = 0

cadastrar = float(input('Quantos produtos a senhora está interessada?'))
for i in range (cadastrar):
    comida = []
    nome = input('Nome do produto')
    valor = float(input('Valor do produto: '))
    marca = input('Marca do produto: ')
    estoque = float(input('Quantidade de estoque do produto'))
    cadastro = (nome, valor, marca, estoque)
    comida.append(nome, valor, marca, estoque)
    saldo = float(input(' Qual o saldo que você possui no momento '))
    troco = calcular_troco(valor, saldo)
    print(f'O produto {nome} com vaor {valor} da marca {marca} e a quantidade do estoque {estoque} com o saldo atual {saldo} terá o troco de {troco}')
    if saldo < valor:
        print('Você não tem saldo o suficiente')
    else:
        print(troco)





    



