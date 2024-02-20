menu = '''
[d] - DEPOSITAR
[s] - SACAR
[e] - EXTRATO
[q] - SAIR

'''

saldo = 0.00
deposito = 0.00
extrato = ''
limite_numero_saques = 3
numero_saques = 0
limite_saque = 500.00
deposito_total = 0.00
saque_total = 0.00


while True:

    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Qual o valor do deposdito a ser realizado'))
        if deposito >= 0:
            saldo += deposito
            deposito_total += deposito
            extrato += f'deposito de R${deposito}\n'
        else:
            print('Impossível depositar valor negativo')

    if opcao == 's':
        valor_saque = float(input('Qual o valor a ser sacado'))
        if (valor_saque <= 500) and (valor_saque <= saldo) and (numero_saques <= limite_numero_saques):
            saldo -= valor_saque
            numero_saques += 1 
            saque_total += valor_saque
            extrato += f'saque de R${valor_saque}\n'
        else:
            print('Não foi possível realizar o saque')

    if opcao == 'e':
        print(f'#################\nDeposito total = {deposito_total}\nSaque Total = {saque_total}\nSaldo = {saldo}')
        
    if opcao == 'q':
        break

    
            