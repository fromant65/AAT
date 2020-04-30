from src.bingo import carton

def test_filas():
	mi_carton=carton()
	for fila in range(0,3):
		for columna in range(0,9):
			for fila2 in range(0,3):
				for columna2 in range(0,9):
					if (fila!=fila2 or columna!=columna2) and mi_carton[fila2][columna2]!=0:
						assert mi_carton[fila2][columna2]!=mi_carton[fila][columna]
