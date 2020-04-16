from src.bingo import carton

def test_filas():
	mi_carton=carton()
	contador=0
	for fila in mi_carton:
		for celda in fila:
			contador+=celda
		assert contador>0
		contador=0
