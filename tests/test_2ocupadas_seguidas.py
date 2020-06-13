from src.bingo import t_2ocupadas_seguidas
from src.bingo import carton1

def test_2ocupadas_seguidas():
    assert t_2ocupadas_seguidas(carton1())
