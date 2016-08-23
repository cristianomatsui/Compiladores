ReservedTokenTable = {'if' : 'IF', 'then' : 'THEN', 'else' : 'ELSE', 'end' : 'END', 'repeat' : 'REPEAT',
               'until' : 'UNTIL', 'read' : 'READ', 'write' : 'WRITE', '+' : 'PLUS', '-' : 'MINUS',
               '*' : 'TIMES', '/' : 'DIV', '=' : 'EQUAL', '<' : 'LESS', '(' : 'LBRACKET',
               ')' : 'RBRACKET', ';' : 'DOTCOMA', ':=' : 'ATRIB'}

# Função que executa leitura do arquivo e atualização dos ponteiros de posição
def read_char(linha, coluna, char, counter, file):
    file.seek(counter)
    counter += 1
    char = file.readline(1)
    coluna += 1
    if char == '\n':        #quebra de linha encontrada --> atualização de contadores de linha e coluna
        linha += 1
        coluna = 0
    return linha, coluna, char, counter

def main():

    archive = input("Insira o nome do arquivo: ")
    file = open(archive, "r")
    char = file.read(1)
    linha = 1
    coluna = 1
    counter = 1     #ponteiro que caminha por dentro do arquivo



    while char:
        if char == '{':         #tratamento de comentários
            while char != '}':
                linha, coluna, char, counter = read_char(linha, coluna, char, counter, file)
                if (not char):
                    print ("Erro: Linha %d Coluna %d, Operador '}' esperado." %(linha, coluna))
                    exit()
        linha, coluna, char, counter = read_char(linha, coluna, char, counter, file)
        print(char)

    file.close()

    return


main()