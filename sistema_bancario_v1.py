def mostrar_contas(lista_contas):
    print("##########LISTA CONTAS##############")
    for lista in lista_contas:
        print(lista)
    
    print("###################################")

def mostrar_usuarios(lista_usarios):
    print("###########LISTA USUARIOS############")
    for lista in lista_usarios:
        print(lista)
    
    print("####################################")

def verificar_usuario(lista_de_usario, cpf):
    #filtro um usuário 
    filtro = [usuario for usuario in lista_de_usario if usuario["cpf"] == cpf]

    return filtro[0] if filtro else None 
            
def criar_usuario(nome, data_nasc, cpf, endereco):

    dict_user = {
        "nome":nome,
        "nascimento":data_nasc,
        "cpf":cpf,
        "endereco":endereco
    }
    
    return dict_user

def criar_conta(*,cpf, num_conta, saldo):
    AGENCIA = "0001"
    num_conta += 1

    conta = AGENCIA + str(num_conta)

    dict_conta ={
            "cpf":cpf,
            "conta":conta,
            "saldo":saldo,
    }

    return dict_conta, num_conta
# keyword only - argumento por nome
def sacar(saldo, valor, extrato, limite_valor ,num_saques, limite_num_saque):

    if saldo>=valor and limite_valor>valor and num_saques<limite_num_saque:
        saldo -=valor
        extrato  += f'''Saque: R${valor: .2f} de R$ {saldo:.2f}\n'''
        num_saques+=1  
    elif saldo<valor:
        print("Saldo Insuficiente")
    elif valor > limite_valor:
        print("Ultrapassou o limite de saque")
    elif num_saques>limite_num_saque:
        print("Ultrapassou o numero de saques permitido")

    return saldo, extrato
    

#positional only - argumento por posicao
def depositar(valor, saldo, extrato,/):
    if valor > 0:
        saldo+=valor
        extrato+=f"Deposito: R$ {valor:.2f}\n"
    else:
        print("Deposito negativo")

    return saldo,extrato


def mostrar_estrato(saldo,/,*,extrato):
    print("\n\n###########EXTRATO###########")
            
    print(extrato)
    print(f"\n\nSaldo: {saldo:.2f}")

    print("################################")


def main():
    LIMITE_VALOR = 500.00
    LIMITE_SAQUE = 3
    opcao = 0
    lista_usuario = []
    lista_contas = []
    saques= 0
    extrato = ""
    saldo = 1500.00
    n_contas = 0

    while True:
        print('''
            [1] - Sacar
            [2] - Depositar
            [3] - Extrato
            [4] - Criar usuario
            [5] - Criar conta
            [6] - Listar usuarios
            [7] - Listar contas
            [8] - Sair
        ''')

        opcao = int(input("Escolha uma das opcões: "))

        match opcao:
            case 1:
                valor = float(input("Digite o valor: "))
                saldo,extrato= sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite_valor=LIMITE_VALOR,
                    limite_num_saque=LIMITE_SAQUE,
                    num_saques=saques)

            case 2:
                valor = float(input("Digite o valor de deposito: "))

                saldo, extrato = depositar(valor,saldo,extrato)
        
            case 3:
                mostrar_estrato(saldo,extrato=extrato)
            case 4:
                nome = input("Digite o seu nome completo: ")
                nascimento = input("Digite sua data de nascimento (ex: xx/xx/xxxx): ")
                cpf = input("Digite seu cpf (xxx.xxx.xxx-xx): ")
                endereco  = input("Digite seu endereco (ex: logradouro - bairro - cidade/sigladoestado): ")

                if verificar_usuario(lista_usuario,cpf) == None:
                    new_user =criar_usuario(nome,nascimento,cpf,endereco)
                    lista_usuario.append(new_user)
                else:
                    print("Usuario existente")

            case 5:

                cpf = input("Digite seu cpf (xxx.xxx.xxx-xx): ")

                if verificar_usuario(lista_usuario,cpf) != None:
                    conta, n_contas = criar_conta(
                        cpf=cpf,
                        num_conta=n_contas,
                        saldo = saldo
                    )

                    lista_contas.append(conta)
                else:
                    print("Usuário não existe")
            case 6:
                mostrar_usuarios(lista_usuario)
            case 7:
                mostrar_contas(lista_contas)
            case 8:
                break
            case _:
                print("O número digitado não está presente no menu")

main()