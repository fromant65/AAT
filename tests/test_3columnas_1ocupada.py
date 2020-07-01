from src.bingo import t_3columnas_1ocupada
from src.bingo import carton1

#Testea que haya 3 y solo 3 columnas con solo una celda ocupada
def test_3columnas_1ocupada():
    assert t_3columnas_1ocupada(carton1())
