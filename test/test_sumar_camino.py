from funciones.sumar_camino import sumar_camino

def test_sumar_camino():
    assert sumar_camino(3, 5) == 8
    assert sumar_camino(-2, 2) == 0