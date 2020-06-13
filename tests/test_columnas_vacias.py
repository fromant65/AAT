from src.bingo import t_columnas_vacias
from src.bingo import carton1

def test_columnas_vacias():
    assert t_columnas_vacias(carton1())
