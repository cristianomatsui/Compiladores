ReservedTokenTable = {'if' : 'IF', 'then' : 'THEN', 'else' : 'ELSE', 'end' : 'END', 'repeat' : 'REPEAT',
               'until' : 'UNTIL', 'read' : 'READ', 'write' : 'WRITE', '+' : 'PLUS', '-' : 'MINUS',
               '*' : 'TIMES', '/' : 'DIV', '=' : 'EQUAL', '<' : 'LESS', '(' : 'LBRACKET',
               ')' : 'RBRACKET', ';' : 'DOTCOMA', ':=' : 'ATRIB'}

NumList = {}
idList = {}

# Função que executa leitura do arquivo e atualização dos ponteiros de posição
def read_char(linha, coluna, counter, file):
    file.seek(counter)
    counter += 1
    char = file.readline(1)
    coluna += 1

    if char == '\n':        #quebra de linha encontrada --> atualização de contadores de linha e coluna
        linha += 1
        coluna = 0

    return linha, coluna, char, counter

def read_id(linha, coluna, char, counter, file):
    file.seek(counter)
    id = ''       #inicia a construção caractere por caractere do identificador

    while (char != ' ') & (char != ''):     #diferente de espaço ou EOF

        if char.isnumeric() | char.isalpha():
            id += char

        elif char:
            print("Erro: Linha %d Coluna %d, identificador inválido." % (linha, coluna))
            exit()

        char = file.readline(1)
        coluna += 1
        counter += 1

    return coluna, counter, id

def read_num(linha, coluna, char, counter, file):
    file.seek(counter)
    num = ''        #inicia a construção dígito a dígito do número

    while (char != ' ') & (char != ''):     #diferente de espaço ou EOF
        if char.isnumeric():
            num += char

        else:
            print("Erro: Linha %d Coluna %d, número inválido." % (linha, coluna))
            exit()

        char = file.readline(1)
        coluna += 1
        counter += 1

    return coluna, counter, num

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
                linha, coluna, char, counter = read_char(linha, coluna, counter, file)
                if not char:        #EOF
                    print ("Erro: Linha %d Coluna %d, Operador '}' esperado." %(linha, coluna))
                    exit()

        elif char.isnumeric():
            coluna, counter, num = read_num(linha, coluna, char, counter, file)
            NumList[num] = len(NumList) +1
            print("<NUM, %d>" %NumList[num], end='')

        elif char.isalpha():
            coluna, counter, id = read_id(linha, coluna, char, counter, file)

            if id not in ReservedTokenTable:
                if id not in idList:
                    idList[id] = len(idList) +1
                    print("<ID, %d>" %idList[id], end='')

                else:
                    print("<ID, %d>" %idList[id], end='')

            else:
                print("<%s>" % ReservedTokenTable[id], end='')

        elif char == ':':
            char += file.read(1)
            counter += 1
            coluna += 1

            if char == ':=':
                print("<%s>" % ReservedTokenTable[char], end='')

        elif char in ReservedTokenTable:
            print("<%s>" %ReservedTokenTable[char], end='')

        linha, coluna, char, counter = read_char(linha, coluna, counter, file)

    file.close()

    return

main()