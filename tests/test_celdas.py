from src.bingo import carton

def test_contar_celdas_ocupadas():
	mi_carton = carton();
	contador=0
	for fila in range(0,3):
		for columna in range(0,9):
                        celda=mi_carton[fila][columna]
                        if celda==0:
                                contador=contador+1
	assert contador==12
	
def test_columnas_ocupadas():
	mi_carton = carton()
	contador=(0,0,0,0,0,0,0,0,0)
	for fila in mi_carton:
		contador=[x + y for x, y in zip(contador, fila)]
	hay_una_vacia=0
	for celda in contador:
		if(celda==0):
			hay_una_vacia=1
	assert hay_una_vacia==0
		
		
