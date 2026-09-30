#iniciando variaveis 
conf=""
num1=""
num2=""


def pergunta():
    print(f"operação selecionada {operacao['esop'][op-1]}")
    while True:
        try:
            num1 = float(input("envie o primeiro valor\n"))
            num2 = float(input("\nenvie o segundo valor\n"))
            return num1, num2
        except ValueError:
            print("valor inválido")



#variavel utilizada para trocar a cor do texto
amarelo ="\033[33m"
normal ="\033[0m "

#criando lista de oprações possíveis
operacao = {
    "escolhas" :[1, 2, 3, 4, 5, 6],
    "esop": ["soma", "subtração", "multiplicação", "divisão", "potência", "raíz quadrada"]}

while conf != "s":
    for escolha, eop in zip(operacao["escolhas"], operacao["esop"]):
        print(f"\n{escolha}: {eop}")
    try:
        op = int(input("escolha o numero com base na operação desejada: "))
    except ValueError:
        print("numero inválido")
        exit()
    conf = input(f"\nvocê escolheu {operacao['esop'][op-1]} caso sua escolha esteja correta digite s caso contrário digite n \n").strip().lower()

match op:
    case 1:
        num1,num2=pergunta()
        print(num1+num2)
    case 2:
        num1,num2=pergunta()
        print(num1-num2)
    case 3:
        num1,num2=pergunta()
        print(num1*num2)
    case 4:
        num1,num2=pergunta()
        print(num1/num2)
    case 5:
        print(f"\n{amarelo}o segundo numero será o valor em que o primeiro numero será elevado  {normal}\n")
        num1,num2=pergunta()
        print(num1**num2)
    case 6:
        num1=float(input("envie o valor "))
        print(f"\nraiz quadra de {num1} = {num1**(1/2)}")
    case _:
        print("opção inválida")