estoque = []

def realizar_venda(qtde_vendida, valor_pago, produto):
        if qtde_vendida > qntde_estoque:
            print('Não pode realizar a venda')
        else:
            valor_pago = float(input('Digite o valor pago'))
            realizar_venda(qtde_vendida, valor_pago, produto)


num = int(input('Digite o número de produtos que quer cadastrar: '))

for i in range(num):
    nome = input('Digite o nome do produto:')
    qntde_estoque = int(input('Digite a quantidade em estoque: '))
    valor = float(input(' Digite o valor do produto:'))
    produto = (nome, qntde_estoque, valor)
    estoque.append(produto)
    qtde_vendida = int(input('Digite a quantidade a ser vendida: '))
    if qtde_vendida > qntde_estoque:
        print('Não pode realizar a venda')
    else:
        valor_pago = float(input('Digite o valor pago'))
        realizar_venda(qtde_vendida, valor_pago, produto)



