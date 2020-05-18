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
	for fila in range(0,3):
		for columna in range(0,9):
			celda= carton[fila][columna]
			aux = aux and (0 <= celda <= 90)
	return aux

def t_contar_celdas_ocupadas(carton):
	contador=0
	for fila in range(0,3):
		for columna in range(0,9):
			celda=carton[fila][columna]
			if celda==0:
				contador+=1
	return contador

def t_columnas_ocupadas(carton):
	contador=(0,0,0,0,0,0,0,0,0)
	for fila in carton:
		contador=[x + y for x, y in zip(contador, fila)]
	hay_una_vacia=0
	for celda in contador:
		if(celda==0):
			hay_una_vacia=1
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

def t_filas(carton):
	contador=0
	aux_bool = True
	for fila in carton:
		for celda in fila:
			contador+=celda
		if contador == 0:
			aux_bool = False
		contador=0
	return aux_bool

def t_incremento_horizontal(carton):
	aux = True
	for fila in range(0,3):
		for columna in range(1,9):
			if carton[fila][columna]<carton[fila][columna-1] and  carton[fila][columna]!=0:
				aux=False
	return aux

def t_num_repetidos(carton):
	aux = True
	for fila in range(0,3):
		for columna in range(0,9):
			for fila2 in range(0,3):
				for columna2 in range(0,9):
					if (fila!=fila2 or columna!=columna2) and carton[fila2][columna2]!=0:
						if carton[fila2][columna2]==carton[fila][columna]:
							aux = False
	return aux