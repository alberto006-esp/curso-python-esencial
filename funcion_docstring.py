def perimetro_cuadrado(Lado):
    """Calcular el perímetro de un cuadrado""" # Descripción corta

    perimetro = Lado * 4
    return perimetro


perimetro_cuadrado(Lado=5)

def perimetro_cuadrado(Lado):
    # Descripción Larga titulo, descripción detallada, argumentos y returns
    """Calcular el perímetro de un cuadrado

    Esta función recibe el valor de un lado de un cuadrado y a partir 
    de este calcula y retorna su perímetro

    Args:
        lado (int): medida del lado del cuadrado
    
    Returns:
        perimetro (int): perimetro del cuadrado
    """
    perimetro = Lado * 4
    return perimetro


perimetro_cuadrado(Lado=5)