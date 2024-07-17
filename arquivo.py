caminho_arq = 'dados.txt'
# Leitura arquivo
with open(caminho_arq, 'r') as arquivo:
    linhas = arquivo.readlines()
 
print("Conteudo original do arquivo")
print(linhas)
 
#Modificação linha
linhas.append("\nEsta é uma nova linha...\n")
 
print("Conteúdo alterado do arquivo:")
print(linhas)
 
#Gravar arquivo
with open(caminho_arq, 'w') as arquivo:
    arquivo.writelines(linhas)
 
print("\nAs alterações foram salvas no arquivo.")