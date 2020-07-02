from src.bingo import t_columnas_3ocupadas
from src.bingo import carton1

#Testea que no haya columnas totalmente ocupadas
def test_columnas_3ocupadas():
    assert t_columnas_3ocupadas(carton1())
