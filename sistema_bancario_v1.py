
saldo = 1000.00
limite = 500.00
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUE = 3
opcao = 0
extrato = ''

def sacar(valor_saque):
    global limite,saldo,numero_saques,extrato

    if valor_saque<=limite and numero_saques<LIMITE_SAQUE and saldo>valor_saque:
        saldo  = saldo - valor_saque
        numero_saques+=1
        extrato +=f"Saque: {valor_saque:.2f}\n"
    elif numero_saques == LIMITE_SAQUE:
        print("Você passou o número de saques possíveis")
    elif valor_saque > saldo:
        print("Você não tem saldo suficiente")
    elif valor_saque > limite:
        print("O valor do saque passou do limite apropriado")

def depositar(valor):
    global saldo, numero_depositos,extrato
    if valor > 0:
        saldo+=valor
        numero_depositos+=1
        extrato+=f"Deposito: {valor:.2f}"
    else:
        print("Deposito negativo")

def mostrar_extrato():
    return "Não tem movimentação" if not extrato else extrato 
    
    

while True:
    print('''
        [1] - Sacar
        [2] - Depositar
        [3] - Extrato
        [4] - Sair
    ''')

    opcao = int(input("Escolha uma das opcões: "))

    if(opcao == 1):
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    elif(opcao==2):
        valor = float(input("Digite o valor de deposito: "))
        depositar(valor)
    elif(opcao==3):
        print("\n\n###########EXTRATO###########")
        
        print(mostrar_extrato())
        print(f"\n\nSaldo: {saldo:.2f}")

        print("################################")
    elif(opcao==4):
        print("FIM DO PROGRAMA")
        break
    else:
        print("O número digitado não está presente no menu")
