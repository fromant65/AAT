from src.bingo import carton


def test_1_a_90():
	mi_carton=carton()
	for fila in range(0,3):
		for columna in range(0,9):
			celda= mi_carton[fila][columna]
			assert celda>=1 and celda <=90

