# Vamos solicitar conom entrada dois números e depois vamos realizar uma operação simples entre eles.

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

operacao = input('Digite a operação que deseja realizar (+, - , *, /): ')

if operacao == "+":
    print(f'Adição: {n1} + {n2} = {n1 + n2}')
elif operacao == "-":
    print(f'Subtração: {n1} - {n2} = {n1 - n2}')
elif operacao == "*":
    print(f'Multiplicação: {n1} * {n2} = {n1 * n2}')
elif operacao == "/":
    print(f'Divisão: {n1} / {n2} = {n1 / n2}')
else:
    print('Opção inválida! Saindo da calculadora!')