from src.bingo import t_contar_celdas_ocupadas
from src.bingo import t_columnas_ocupadas
from src.bingo import carton2

#Testea que haya 15 celdas ocupadas
def test_contar_celdas_ocupadas():
	assert t_contar_celdas_ocupadas(carton2()) == True

#Testea que todas las columnas estén ocupadas
def test_columnas_ocupadas():
	assert t_columnas_ocupadas(carton2()) == True
