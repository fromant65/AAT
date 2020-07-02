from src.bingo import t_filas
from src.bingo import carton2

#Testea que no haya filas vacias
def test_filas():
	assert t_filas(carton2()) == True