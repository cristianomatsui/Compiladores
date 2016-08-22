
def read_char(linha, coluna, char, counter):
    file.seek(counter)
    counter += 1
    char = file.readline(1)
    coluna += 1
    if char == '\n':
        linha += 1
    return

archive = input("Insira o nome do arquivo: ")
file = open(archive, "r")
char = file.read(1)
linha = 1
coluna = 30
counter = 1


while char:
    if char == '{':         #tratamento de comentários
        while char != '}':
            read_char(linha, coluna, char, counter)
            if (not char):
                print ("Erro: Linha %d Coluna %d, Operador '}' esperado." %(linha, coluna))
                exit(-1)

    read_char(linha, coluna, char, counter)

file.close()
