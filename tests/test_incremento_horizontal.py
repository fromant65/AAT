from src.bingo import t_incremento_horizontal
from src.bingo import carton1

def test_incremento_horizontal():
    assert t_incremento_horizontal(carton1()) == True

