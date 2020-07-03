from src.bingo import elegirCarton

def mostrar_carton():
    carton = elegirCarton()
    pal=""
    for i in range(3):
        for j in range(9):
            pal = pal + '[' + str(carton[i][j]) + '] '
        pal = pal + '\n'
    return pal


def t_mostrar_carton():
    carton=mostrar_carton()
    template= "[][][][][][][][][][][][][][][][][][][][][][][][][][][]"
    pal=""
    for fila in carton:
        for chr in fila:
            if chr == '[' or chr == ']':
                pal=pal+chr
    if pal==template:
        return True
    else:
        return False

#print(t_mostrar_carton())
print(mostrar_carton())

