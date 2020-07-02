from src.bingo import t_2vacias_seguidas
from src.bingo import carton1

#Testea que haya hasta 2 celdas vacias seguidas
def test_2vacias_seguidas():
    assert t_2vacias_seguidas(carton1())
