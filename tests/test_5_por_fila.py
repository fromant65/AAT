from src.bingo import t_5_por_fila
from src.bingo import carton2

#Testea que haya 5 numeros por fila
def test_5_por_fila():
    assert t_5_por_fila(carton2())
