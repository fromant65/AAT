from src.bingo import t_columnas_descendentes
from src.bingo import carton1

def test_columnas_descendentes():
    assert t_columnas_descendentes(carton1()) == True
