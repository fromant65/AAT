from src.bingo import t_3columnas_1ocupada
from src.bingo import carton1

def test_3columnas_1ocupada():
    assert t_3columnas_1ocupada(carton1())
