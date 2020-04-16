from src.bingo import carton

def test_contar_celdas_ocupadas():
	mi_carton = carton();
	contador = 0
	for fila in mi_carton:
		for celda in fila:
			contador=contador+celda
	assert contador==15
def test_celdas_no_menor_15():
	mi_carton = carton();
	contador = 0
	for fila in mi_carton:
		for celda in fila:
			contador=contador+celda
	assert contador>14
def test_celdas_no_mayor_15():
	mi_carton = carton()
	contador = 0
	for fila in mi_carton:
		for celda in fila:
			contador=contador+celda
	assert contador<16
	
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
		
		
