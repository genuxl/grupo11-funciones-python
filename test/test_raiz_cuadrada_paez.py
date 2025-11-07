#tests/test_raiz_cuadrada.py
from funciones.funcion_raiz_cuadrada_paez import raiz_cuadrada
def test_raiz_cuadrada():
 assert raiz_cuadrada(9) == 3
 assert raiz_cuadrada(-4) is None