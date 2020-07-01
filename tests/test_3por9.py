from src.bingo import t_3por9
from src.bingo import carton1

#Testea que el carton sea una matriz de 3*9
def test_3por9():
    assert t_3por9(carton1())
