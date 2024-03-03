import textwrap

def exibir_menu():
    menu = '''
[d] -  DEPOSITAR
[s] -  SACAR
[e] -  EXTRATO
[nu] - CRIAR NOVO USUARIO
[nc] - CRIAR NOVA CONTA
[lc] - LISTAR CONTAS
[q] -  SAIR

'''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito >= 0:
        saldo += valor_deposito
        #deposito_total += valor_deposito
        extrato += f'deposito de R${valor_deposito:.2f}\n'
        print('Depósito realizado!')
    else:
        print('Falha! Valor inválido!')
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor_saque > saldo
    excedeu_saques = numero_saques > limite_saques
    excedeu_limite = valor_saque > limite

    if excedeu_saldo:
        print('Falha! Saldo Insuficiente!')

    elif excedeu_limite:
        print('Falha! Limite Insuficiente')

    elif excedeu_saques:
        print('Falha! Numero de saques permitidos excedido!')

    elif(valor_saque > 0):    
        saldo -= valor_saque
        #saque_total += valor_saque
        extrato += f'saque de R${valor_saque}\n'
        numero_saques += 1
        print('Saque realizado com sucesso')

    else:
        print('Falha! Valor invalido') 
        

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('SEM MOVIMENTAÇÕES' if not extrato else extrato)
    print(f'\nSALDO\nSaldo = {saldo}')

def criar_usuario(usuarios):
    cpf = input('Digite o CPF do usuário a ser cadastrado:')
    usuario = filtrar_cpf(cpf, usuarios)

    if usuario:
        print('Usuario já cadastrado!')

        return
    else:
        nome = input('Digite o nome a ser cadastrado: ')
        data_nascimento = input('Digite a data de nascimento: ')
        endereco = input('Digite o endereço:[logradouro - nro - bairro - cidade/sigla estado] ')

        usuarios.append({"nome": nome, "data nascimento ": data_nascimento, "cpf": cpf, "endereço": endereco})
        print('usuario criado com sucesso')

def filtrar_cpf(cpf, usuarios): 
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o cpf do usuário: ")
    usuario = filtrar_cpf(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {"Agencia": agencia, "Conta": numero_conta, "usuario": usuario}


    else:
        print('Falha! Necessario criar usuario!')

def listar_contas(contas):
    for conta in contas:
        print(f'Agencia:{conta["Agencia"]}\nConta:{conta["Conta"]}\nCliente:{conta["usuario"]["nome"]} ')


def main():
    limite_saques = 3
    AGENCIA = "0001"

    saldo = 0.00
    limite = 500.00
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:

        opcao = exibir_menu()

        if opcao == 'd':
            valor_deposito = float(input('Qual o valor do deposdito a ser realizado'))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == 's':
            valor_saque = float(input('Qual o valor a ser sacado'))
            saldo, extrato = sacar(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
            
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('opcao não listada, escolha novamente')




main()




            
            





