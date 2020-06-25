import random

def carton1():
	carton = (
		(1,10,22,0,0,54,0,72,0),
		(2,12,0,35,43,0,61,0,82),
		(0,0,25,0,47,58,0,79,0)
	)
	return carton

def carton2():
	carton = (
		(1, 0, 0, 0, 1, 0, 1, 1, 1),
		(1, 1, 0, 1, 0, 1, 0, 0, 1),
		(0, 1, 1, 0, 1, 0, 1, 0, 1),
	)
	return carton

def t_1_a_90(carton):
	aux = True
	for fila in carton:
		for celda in fila:
			aux = aux and (0 <= celda <= 90)
	return aux

def t_contar_celdas_ocupadas(carton):
	contador=0
	for fila in carton:
		for celda in fila:
			if celda==0:
				contador+=1
	return (contador==12)

def t_columnas_ocupadas(carton):
	contador=[0,0,0,0,0,0,0,0,0]
	for fila in range(3):
		for celda in range(9):
		    contador[celda] = carton[fila][celda]
	hay_una_vacia=False
	for celda in contador:
		if(celda==0):
			hay_una_vacia=True
	return hay_una_vacia

def t_columnas_descendentes(carton):
	aux=[0,0,0,0,0,0,0,0,0,0] #Matriz auxiliar para comparar columna por columna
	aux_bool=True
	for fila in range(0,3):
		for columna in range(0,9):
			if carton[fila][columna]>aux[columna] and carton[fila][columna]!=0: #Si la celda actual es mayor a su inmediata posterior y no está vacia
				aux[columna]=carton[fila][columna] #La guardamos en la matriz auxiliar
			elif carton[fila][columna]==0:
				pass
			else:
				aux_bool = False
	return aux_bool

def t_filas(carton): #Verifica que no haya filas vacias
	contador=0
	aux_bool = True
	for fila in carton:
		for celda in fila:
			contador+=celda
		if contador == 0:
			aux_bool = False
		contador=0
	return aux_bool

def t_incremento_horizontal(carton): #Verifica que los numeros del carton crezcan de menor a mayor en las filas
	aux = True
	for fila in range(0,3):
		for columna in range(1,9):
			if carton[fila][columna]<carton[fila][columna-1] and carton[fila][columna]!=0:
				aux=False
	return aux

def t_num_repetidos(carton): #Verifica que no haya numeros repetidos en el carton
	aux = True
	for fila in range(0,3):
		for columna in range(0,9):
			for fila2 in range(0,3):
				for columna2 in range(0,9):
					if (fila!=fila2 or columna!=columna2) and carton[fila2][columna2]!=0:
						if carton[fila2][columna2]==carton[fila][columna]:
							aux = False
	return aux

def t_5_por_fila(carton): #Verifica que haya 5 casillas ocupadas x fila
    contador = 0;
    bandera = True
    for fila in carton:
        contador=0
        for celda in fila:
            if celda!=0:
                contador+=1
        if contador!=5:
            bandera = False
    return bandera

def t_3por9(carton): #Verifica que el carton sea una matriz de 3*9
    c1=0
    c2=0
    bandera= False
    for fila in carton:
        c1+=1
        for celda in fila:
            c2+=1
    if c1==3 and c2==27:
        bandera=True
    return bandera

def t_columnas_vacias(carton): #Verifica que no haya columnas vacias
    aux=[0,0,0,0,0,0,0,0,0]
    for fila in range(3):
        for celda in range (9):
            aux[celda]+=carton[fila][celda]
    bandera=True
    for celda in aux:
        if(celda==0):
            bandera=False
    return bandera

def t_columnas_3ocupadas(carton): #Verifica que las 3 celdas de cada columna no esten llenas
    bandera=True
    for celda in range(9):
        if carton[0][celda]!=0 and carton[1][celda]!=0 and carton[2][celda]!=0:
            bandera=False
    return bandera

def t_3columnas_1ocupada(carton): #Verifica que solo haya 3 columnas con una sola casilla ocupada
    aux=[0,0,0,0,0,0,0,0,0]
    contador=0
    bandera=False
    for celda in range(9):
        if (carton[0][celda] != 0 and carton[1][celda] == 0 and carton[2][celda] == 0) or (carton[0][celda] == 0 and carton[1][celda] != 0 and carton[2][celda] == 0) or (carton[0][celda] == 0 and carton[1][celda] == 0 and carton[2][celda] != 0):
            aux[celda]+=1
    for celda in range(9):
        contador+=aux[celda]
    if contador==3:
        bandera=True
    return bandera

def t_2vacias_seguidas(carton): #Verifica que no haya mas de 3 celdas consecutivas vacias en el carton
    bandera=True
    for fila in range(3):
        for celda in range(7):
            if carton[fila][celda]==0 and carton[fila][celda+1]==0 and carton[fila][celda+2]==0:
                bandera= False
    return bandera

def t_2ocupadas_seguidas(carton): #Verifica que no haya mas de 3 celdas consecutivas ocupadas en el carton
    bandera=True
    for fila in range(3):
        for celda in range(7):
            if carton[fila][celda]!=0 and carton[fila][celda+1]!=0 and carton[fila][celda+2]!=0:
                bandera= False
    return bandera

def intentoCarton():
    contador = 0
    carton = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    numerosCarton = 0

    while numerosCarton < 15:
        contador+=1
        if (contador == 50):
            return intentoCarton()

        numero = random.randint (1, 90)

        columna = numero // 10
        if (columna == 9):
            columna = 8
        huecos = 0
        for i in range(3):
            if carton[columna][i] == 0:
                huecos+=1
            if carton[columna][i] == numero:
                huecos = 0
                break
        if huecos < 2:
            continue
        fila = 0
        for j in range(3):
            huecos = 0
            for i in range(9):
                if (carton[i][fila] == 0):
                    huecos+=1
            if huecos < 5 or carton[columna][fila] != 0:
                fila+=1
            else:
                break
        if (fila == 3):
            continue

        carton[columna][fila] = numero
        numerosCarton+=1
        contador = 0

    for x in range(9):
        huecos = 0
        for y in range(3):
            if carton[x][y] == 0:
                huecos+=1
        if huecos == 3:
            return intentoCarton()
    return carton

def intentoATests(): #Pasa un carton de intentoCarton() a uno para hacer tests
    carton=intentoCarton()
    carton2=[
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    for i in range(9):
        for j in range (3):
            carton2[j][i]=carton[i][j]
    return carton2

#for i in range(50):
#    print (intentoATests())

def elegirCarton():
    i=0
    while True:
        carton=intentoATests()
        i+=1
        #print(t_columnas_descendentes(carton))
        if t_3por9(carton) and t_1_a_90(carton) and t_contar_celdas_ocupadas(carton) and t_columnas_ocupadas(carton) and t_columnas_descendentes(carton) and t_filas(carton) and t_incremento_horizontal(carton) and t_num_repetidos(carton) and t_5_por_fila(carton) and t_columnas_vacias(carton) and t_columnas_3ocupadas(carton) and t_3columnas_1ocupada(carton) and t_2vacias_seguidas(carton) and t_2ocupadas_seguidas(carton):
            print(i)
            break
    return carton

print (elegirCarton())