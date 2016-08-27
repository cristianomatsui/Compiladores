# Aluno: Cristiano Matsui  --  RA: 1585444  --  CO28CP 2016-02
# Programa feito em Python 3.5

ReservedTokenTable = {'if' : 'IF', 'then' : 'THEN', 'else' : 'ELSE', 'end' : 'END', 'repeat' : 'REPEAT',
               'until' : 'UNTIL', 'read' : 'READ', 'write' : 'WRITE', '+' : 'PLUS', '-' : 'MINUS',
               '*' : 'TIMES', '/' : 'DIV', '=' : 'EQUAL', '<' : 'LESS', '(' : 'LBRACKET',
               ')' : 'RBRACKET', ';' : 'DOTCOMA', ':=' : 'ATRIB'}       #Dicionário de palavras reservadas

NumDict = {}        #Dicionário de números lidos
idDict = {}         #Dicionário de identificadores lidos

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
    ERRFLAG = 0

    while (char != ' ') & (char != ''):     #diferente de espaço ou EOF

        if char.isnumeric() | char.isalpha():
            id += char

        elif char:
            id = ("\nErro: Linha %d Coluna %d, identificador inválido." % (linha, coluna))
            ERRFLAG = 1
            while (char != ' ') & (char != ''):     #Leitura do restante do id, apenas para avanço de contadores
                char = file.readline(1)
                coluna += 1
                counter += 1
            return coluna, counter, id, ERRFLAG

        char = file.readline(1)
        coluna += 1
        counter += 1

    return coluna, counter, id, ERRFLAG

def read_num(linha, coluna, char, counter, file):
    file.seek(counter)
    num = ''        #inicia a construção dígito a dígito do número
    ERRFLAG = 0

    while (char != ' ') & (char != ''):     #diferente de espaço ou EOF
        if char.isnumeric():
            num += char

        else:
            num = ("\nErro: Linha %d Coluna %d, número inválido." % (linha, coluna))
            ERRFLAG = 1
            while (char != ' ') & (char != ''):      #Leitura do restante do número, apenas para avanço de contadores
                char = file.readline(1)
                coluna += 1
                counter += 1
            return coluna, counter, num, ERRFLAG

        char = file.readline(1)
        coluna += 1
        counter += 1

    return coluna, counter, num, ERRFLAG

def main():

    archive = input("Insira o nome do arquivo: ")
    file = open(archive, "r")
    char = file.read(1)
    linha = 1
    coluna = 1
    counter = 1     #ponteiro que caminha por dentro do arquivo

    FLAG_ERROR = 0      #Flag que sinaliza se ocorreu algum erro de compilação
    ErrorMessages = ''
    CompilerExit = ''

    while char:
        if char == '{':         #tratamento de comentários
            while char != '}':
                linha, coluna, char, counter = read_char(linha, coluna, counter, file)
                if not char:        #EOF
                    ErrorMessages += ("\nErro: Linha %d Coluna %d, Operador '}' esperado." %(linha, coluna))
                    FLAG_ERROR = 1

        elif char.isnumeric():
            coluna, counter, num, ERRFLAG = read_num(linha, coluna, char, counter, file)
            if ERRFLAG == 0:
                NumDict[num] = len(NumDict) +1
                CompilerExit += ("<NUM, %d>" %NumDict[num])

            else:
                ErrorMessages += num
                FLAG_ERROR = 1

        elif char.isalpha():
            coluna, counter, id, ERRFLAG = read_id(linha, coluna, char, counter, file)

            if ERRFLAG == 0:

                if id not in ReservedTokenTable:
                    if id not in idDict:
                        idDict[id] = len(idDict) +1
                        CompilerExit += ("<ID, %d>" %idDict[id])

                    else:
                        CompilerExit += ("<ID, %d>" %idDict[id])

                else:
                    CompilerExit += ("<%s>" % ReservedTokenTable[id])

            else:
                ErrorMessages += id
                FLAG_ERROR = 1


        elif char == ':':
            char += file.read(1)
            counter += 1
            coluna += 1

            if char == ':=':
                CompilerExit += ("<%s>" % ReservedTokenTable[char])

            else:
                ErrorMessages += ("\nErro: Linha %d Coluna %d. Sintaxe ou comando errado." %(linha, coluna))
                FLAG_ERROR = 1

        elif char in ReservedTokenTable:
            CompilerExit += ("<%s>" %ReservedTokenTable[char])

        linha, coluna, char, counter = read_char(linha, coluna, counter, file)

    if FLAG_ERROR == 1:
        print (ErrorMessages)

    else:
        print (CompilerExit)

    file.close()

    return

main()