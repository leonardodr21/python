
retorno = 1


planos = {
    "nomes": ["plano mensal", "plano trimestral", "plano anual"],
    "precos": [100, 270, 1000]
}

def salvar_alunos(nome, plano, idade, cpf):
    with open ("../data/alunos.csv", "a") as arquivo:
                arquivo.write(f"Nome: {nome} | Plano: {plano} | Idade: {idade} | CPF: {cpf}\n")

def consultar_planos():
    for i, (nome, preco) in enumerate(zip(planos["nomes"], planos["precos"])):
        print(f"\n{i+1} - {nome}: {preco}R$\n")


def consultar_aluno(pesquisa):
    pesquisa = pesquisa.strip().lower()
    encontrado = False
    with open("../data/alunos.csv", "r") as arquivo:
        for linha in arquivo:
            if pesquisa in linha.lower():
                print(f"Aluno encontrado: {linha.strip()}")
                encontrado = True
        if not encontrado:
            print("aluno não encontrado")

            

def cadastro_aluno():

    nome = input ("\ndigite o nome do aluno:\n").strip().lower()
    try:
        idade = int(input("\ndigite a idade do aluno:\n").strip())
    except ValueError:
        print("idade inválida")
        return
    cpf = input("digite o CPF do aluno:\n").strip()

    consultar_planos()

    plano = input("digite o plano escolhido: ").strip().lower()
    if plano in ["1", "2", "3"]:
        plano = planos["nomes"][int(plano) - 1] 
    else:
        print("plano inválido, tente novamente.")
        return
            
    salvar_alunos(nome, plano, idade, cpf)
    print("aluno cadastrado com sucesso!")
    print(f"aluno: {nome} - plano: {plano} - idade: {idade} - CPF: {cpf}")


while retorno != 0:
    print("\nbem vindo a academia generica\n")
    opcao = input ("\nqual opção deseja realizar? \n1- consultar planos \n2- consultar aluno \n3- cadastrar aluno \n4- sair\n")
    if opcao == "1":   
        consultar_planos()
        input()

    elif opcao == "2":  # opção do menu para consultar alunos
        pesquisa = input("digite o nome do aluno ").strip().lower()
        consultar_aluno(pesquisa)
    elif opcao == "3":# opção do menu para cadastrar alunos 
        while True:
            cadastro_aluno()

            
            v3 = input("selecione uma opção:\n1- para cadastrar outro aluno,\n2- para sair,\n3- para retornar ao menu: ").strip().lower()
            if v3 == "1":
                continue
            elif v3 == "2":
                print("saindo do programa...\n")
                retorno = 0
                break
            else:
                print("\nretornando ao menu...\n")
                break
        
    elif opcao == "4":
        print("\nsaindo do programa...\n")
        retorno = 0   
        break
    else:
        print("opção inválida, tente novamente.")
