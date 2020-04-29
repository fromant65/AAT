from src.bingo import carton

def test_incremento_horizontal():
	mi_carton= carton()
	for fila in range(0,3):
		aux=0
		for columna in range(1,9):
			if mi_carton[fila][columna]<mi_carton[fila][columna-1] and  mi_carton[fila][columna]!=0: 
				aux=aux+1
		assert aux==0
