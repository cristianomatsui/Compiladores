def main():
    def read_char(linha, coluna, char, counter):
        file.seek(counter)
        counter += 1
        char = file.readline(1)
        coluna += 1
        if char == '\n':
            linha += 1
        return linha, coluna, char, counter

    archive = input("Insira o nome do arquivo: ")
    file = open(archive, "r")
    char = file.read(1)
    linha = 1
    coluna = 1
    counter = 1


    while char:
        if char == '{':         #tratamento de comentários
            while char != '}':
                linha, coluna, char, counter = read_char(linha, coluna, char, counter)
                if (not char):
                    print ("Erro: Linha %d Coluna %d, Operador '}' esperado." %(linha, coluna))
                    exit("Error")

        linha, coluna, char, counter = read_char(linha, coluna, char, counter)

    file.close()


main()