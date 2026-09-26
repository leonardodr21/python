nomes = ["leo","lanna","lucas","davi"]

print(nomes[1])
print(nomes)
nomes.append("maria")
nomes.remove("lucas")
print(nomes)
print(nomes[3])
print(nomes[0:2])
print(nomes[-2])
nomes.insert(1,"joao")
print(sorted(nomes))
print(list(reversed(nomes)))
nomes[4] = "lucas"
print(nomes)
nomes[1] = "lanna"#sobrepõe o valor do indice 1
print(nomes)

numeros = [1,34,6,8,5]
print(list(reversed(numeros)))
nome=("leonardo", "lanna", "lucas", "davi") #tupla - imutável
print(nome[1])
print(nome)
# nome[1] = "maria" # isso causaria um erro, pois tuplas são imutáveis

# lista de preços de eletrodomésticos com 5 elementos
precos = [202.1, 101, 304, 503.1, 1004.01]
# len retorna a quantidade de elementos
print(len(precos))
# sorted retorna a lista ordenada
print(sorted(precos))
# reversed inverte a ordem
print(reversed(precos))
# list inverte a ordem
print(list(reversed(precos)))
# sum soma os elementos
print(sum(precos))
# min retorna ao menor elemento
print(min(precos))
# max retorna o maior elemento
print(max(precos))

 #dicionário - coleção de pares chave-valor
notas = {"leonardo": 8.5,
         "lanna": 9.0,
         "lucas": 7.5,
         "davi": 8.0
}   
print(notas)
print(notas["lanna"])
print(notas.keys())
print(notas.values())
print(notas.items())    


qtd_produtos = {"leonardo": 3,
                 "lanna": 5,    
                "lucas": 2,}

print(qtd_produtos)
print(type(qtd_produtos))

sel = input("Digite o nome do aluno: ")
sel= sel.strip().lower() #remove espaços e converte para minúsculo
print(qtd_produtos.get(sel, "Aluno não encontrado"))
print(qtd_produtos["lucas"] + 5)

print(qtd_produtos)

#dicionario com lista como valor
televisores ={
    "marcas" : ["samsung","LG","panasonic"],
    "preco": [10000, 3000, 1000],
    "tamanho": [32, 42, 50],
    "quantidade" : [22, 30, 5]

}

for chave, valor in televisores.items():
    print(f"{chave}: {valor}")
#%%
