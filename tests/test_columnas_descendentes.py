from src.bingo import carton

def test_columnas_descendentes():
	mi_carton=carton()
	aux=[0,0,0,0,0,0,0,0,0,0] #Matriz auxiliar para comparar columna por columna
	for fila in range(0,3):
		for columna in range(0,9):
			if mi_carton[fila][columna]>aux[columna] and mi_carton[fila][columna]!=0: #Si la celda actual es mayor a su inmediata posterior y no está vacia 
				aux[columna]=mi_carton[fila][columna] #La guardamos en la matriz auxiliar
			elif mi_carton[fila][columna]==0: #Si la celda está vacia
				aux[columna]=0 #Guardamos su valor
			else:
				aux[columna]=-1 #Si la celda no está vacia y no es mayor a la de arriba guardamos -1
			assert aux[columna]>-1 #Asumimos que si el carton es correcto ninguna celda en la matriz auxiliar será -1
