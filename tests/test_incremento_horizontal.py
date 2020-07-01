from src.bingo import t_incremento_horizontal
from src.bingo import carton1

#Testea que los numeros crezcan horizontalmente de izquierda a derecha
def test_incremento_horizontal():
    assert t_incremento_horizontal(carton1()) == True

