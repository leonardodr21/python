conf=""

#variavel utilizada para trocar a cor do texto
amarelo ="\033[33m"
normal ="\033[0m "

operacao = {
    "escolhas" :[1, 2, 3, 4, 5, 6],
    "esop": ["soma", "subtração", "multiplicação", "divisão", "potência", "raíz quadrada"]}

while conf != "s":
    for escolha, eop in zip(operacao["escolhas"], operacao["esop"]):
        print(f"\n{escolha}: {eop}")
    print(f"\n{amarelo}caso escolha potencia o segundo numero será o valor em que o primeiro numero será elevado  {normal}\n")
    print(f"{amarelo}caso escolha raiz quadrada o segundo numero será desconsiderado{normal}\n")
    try:
        op = int(input("escolha o numero com base na operação desejada: "))
    except ValueError:
        print("numero inválido")
        exit()
    conf = input(f"\nvocê escolheu {op} caso sua escolha esteja correta digite s caso contrário digite n \n").strip().lower()

if op in range(1, 7):

    print(f"operação selecionada {operacao['esop'][op-1]}")
    num1 = float(input("envie o primeiro valor"))
    print("")
    num2 = float(input("envie o segundo valor"))
    if op == 1 : 
        print(num1+num2)

    elif op == 2:
        print(num1-num2)

    elif op == 3:
        print(num1*num2)

    elif op == 4:
        if num2 !=0:
            print(num1 / num2)
        else:
            print("não é possível dividir por zero")

    elif op == 5:
        print(num1**num2)

    elif op == 6:
        print(num1**(1/2))
else:
    print("opcção invalida")
