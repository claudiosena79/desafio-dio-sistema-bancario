import textwrap

def main():
    saldo = 0.00
    extrato = ""
    limite = 500.00
    numero_saques = 1
    limite_saques = 3
    usuarios = []
    AGENCIA = 1
    numero_da_conta = 1
    contas = []

    while True:

        opcao = exibir_menu()

        if opcao == 'd':
            deposito = float(input('Digite o valor a ser depositado[R$]: '))
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == 's':
            saque = float(input('Digite o valor a ser sacado[R$]: '))
            saldo, extrato = sacar(saldo=saldo, saque=saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            cpf = input('Digite o CPF do usuario a ser cadastrado: ')
            criar_usuario(cpf, usuarios)

        elif opcao == 'nc':
            cpf = input('Digite o CPF do usuário ligado a nova conta: ')
            usuario = filtrar_usuarios_cpf(cpf, usuarios)
            if usuario:
                conta=criar_conta(AGENCIA, numero_da_conta, usuario)
                contas.append(conta)                    
            else:
                print("CPF NÃO CADASTRADO, UTILIZE A OPÇÃO nu! ")

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print("OPÇÃO INVALIDA")

def exibir_menu():
    menu = '''
    [d]  - DEPOSITAR
    [s]  - SACAR
    [e]  - EXTRATO
    [nu] - CRIAR NOVO USUARIO
    [nc] - CRIAR NOVA CONTA
    [lc] - LISTAR CONTAS
    [q]  - SAIR

    Qual opcão escolhida? 
    '''
    return input(textwrap.dedent(menu))

def depositar(saldo, deposito, extrato,/):
    if deposito > 0:
        saldo += deposito
        extrato = f'Depósito de R${deposito}'
        print("DEPÓSITO REALIZADO COM SUCESSO")
    else:
        print("DEPÓSITO NÃO REALIZADO, VALOR INCORRETO")
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = saque > saldo
    excedeu_saques = numero_saques > limite_saques
    excedeu_limite = saque > limite

    if excedeu_saldo:
        print("SALDO INSUFICIENTE, SAQUE NÃO REALIZADO\n")
    elif excedeu_limite:
        print("LIMITE EXCEDIDO, SAQUE NÃO REALIZADO\n")
    elif excedeu_saques:
        print("NÚMERO DE SAQUES EXCEDIDO\n")
    elif saque > 0:
        saldo -= saque
        extrato = f'Saque de R${saque}'
        print("SAQUE REALIZADO COM SUCESSO")
    else:
        print("SAQUE NÃO REALIZADO, VALOR INCORRETO")
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("SEM MOVIMENTAÇÕES" if not extrato else extrato)
    print(f'SALDO:\nSaldo : {saldo:.2f}')

def criar_usuario(cpf, usuarios):
    usuario = filtrar_usuarios_cpf(cpf, usuarios)
    if usuario:
        print("USUÁRIO JÁ CADASTRADO")
        return
    else:
        nome = input('Digite o nome do novo usuário: ')
        data_nascimento = input('Digite sua data de nascimento[dd/mm/aaaa]: ')
        endereco = input('Digite seu endereço[logradouro - bairro - cidade - UF]')
        usuarios.append({"NOME": nome, "NASCIMENTO": data_nascimento, "CPF": cpf, "ENDERECO": endereco})
        print("USUARIO CRIADO COM SUCESSO")

def filtrar_usuarios_cpf(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario['CPF'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(AGENCIA, numero_da_conta, usuario):
    conta = {"Agencia":AGENCIA, "C/C":numero_da_conta, "USUARIO":usuario}
    numero_da_conta += 1
    print("CONTA CRIADA COM SUCESSO")
    return conta

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['Agencia']}\nC/C: {conta['C/C']}\nCliente: {conta['USUARIO']['NOME']}")

main()

