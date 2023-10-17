def calcular_imc(peso, altura):
    imc = peso / (altura **2)
    return imc
pessoas = []
i = 0
cadastrar = int(input('Quantas vezes quer cadastrar: '))
for i in range (cadastrar):
    nome = input(f'Digite o nome da pessoa {i+1}:')
    idade = int(input(f'Digite a idade da pessoa {i+1}:'))
    peso = float(input(f'Coloque o seu peso aqui {i+1}:'))
    altura = float(input(f'Coloque sua altura aqui {i+1}:'))

    cadastro = ({nome}, {idade}, {peso}, {altura})
    pessoas.append(cadastro)
    imc = calcular_imc(peso, altura)
    print(f'A pessoa {nome} com idade {idade} peso {peso} e altura {altura} tem o IMC = {imc:.2f}')
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 24.9:
        print('Peso normal')
    elif 25 <= imc <29.9:
        print('Sobrepeso')
    elif 30 <= imc < 34.9:
        print('Obesidade grau I') 
    elif 35 <= imc < 39.9:
        print('Obesidade grau II')
    else:
        print('Obesidade grau III') 
    print(f'Seu IMC é: {imc}')
