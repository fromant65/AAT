from src.bingo import t_contar_celdas_ocupadas
from src.bingo import t_columnas_ocupadas
from src.bingo import carton2

def test_contar_celdas_ocupadas():
	assert t_contar_celdas_ocupadas(carton2()) == True

def test_columnas_ocupadas():
	assert t_columnas_ocupadas(carton2()) == True
