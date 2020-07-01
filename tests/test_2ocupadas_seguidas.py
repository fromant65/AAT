from src.bingo import t_2ocupadas_seguidas
from src.bingo import carton1

#Testea que haya hasta 2 celdas ocupadas seguidas
def test_2ocupadas_seguidas():
    assert t_2ocupadas_seguidas(carton1()) == True
