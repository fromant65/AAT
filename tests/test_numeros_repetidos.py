from src.bingo import t_num_repetidos
from src.bingo import carton1

def test_num_repetidos():
    assert t_num_repetidos(carton1()) == True

