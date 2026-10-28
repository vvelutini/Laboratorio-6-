def parsear_producto(linea: str):
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        dict: {"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}
    """
    if not isinstance(linea, str):
        raise ValueError("La linea debe ser un str")

    partes = linea.split(",")
    if len(partes) != 4:
        raise ValueError("La linea debe tener exactamente 4 elementos")

    codigo = partes[0].strip()
    nombre = partes[1].strip()
    precio = partes[2].strip()
    cantidad = partes[3].strip()

    try:
        precio = float(precio)
    except ValueError:
        raise ValueError("El precio debe ser un numero")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    try:
        cantidad = int(cantidad)
    except ValueError:
        raise ValueError("La cantidad debe ser un entero")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")

    return {"codigo": codigo, "nombre": nombre, "precio": precio, "cantidad": cantidad}


def resumen_de_producto(linea: str) -> str:
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        str: "CODIGO - NOMBRE: $VALOR" (VALOR = precio*cantidad redondeado a 1 decimal)
    """
    producto = parsear_producto(linea)
    codigo = producto["codigo"]
    nombre = producto["nombre"]
    precio = producto["precio"]
    cantidad = producto["cantidad"]

    valor = round(precio * cantidad, 1)

    return f"{codigo} - {nombre}: ${valor}"


def _validar_lineas(lineas: list):
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        None. Levanta ValueError si lineas no es una lista no vacía de str.
    """
    if not isinstance(lineas, list) or len(lineas) == 0:
        raise ValueError("lineas debe ser una lista no vacia")

    for linea in lineas:
        if not isinstance(linea, str):
            raise ValueError("Cada elemento de lineas debe ser un str")


def resumen_de_lotes(lineas: list) -> list:
    """
    Entrada:
        lines: list de str, no vacía
    Salida:
        list de str con resúmenes por producto (usa resumen_de_producto)
    """
    _validar_lineas(lineas)

    salida = []
    for linea in lineas:
        salida.append(resumen_de_producto(linea))

    return salida


def valor_de_lote(lineas: list) -> float:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        float: valor total (suma de precio*cantidad) redondeado a 1 decimal
    """
    _validar_lineas(lineas)

    total = 0.0
    for linea in lineas:
        producto = parsear_producto(linea)
        total += producto["precio"] * producto["cantidad"]

    return round(total, 1)


def producto_maximo_valor(lineas: list) -> str:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        str: resumen del producto de mayor (precio*cantidad). En empate, el primero.
    """
    _validar_lineas(lineas)

    mejor = parsear_producto(lineas[0])
    mejor_valor = mejor["precio"] * mejor["cantidad"]

    for linea in lineas[1:]:
        producto = parsear_producto(linea)
        valor = producto["precio"] * producto["cantidad"]
        if valor > mejor_valor:
            mejor = producto
            mejor_valor = valor

    valor_redondeado = round(mejor_valor, 1)

    return f"{mejor['codigo']} - {mejor['nombre']}: ${valor_redondeado}"


if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10"
    ]
    print(resumen_de_producto(products[0]))       # "P001 - Lapiz: $50.0"
    print(resumen_de_lotes(products))             # ["P001 - ...", "P002 - ...", "P003 - ..."]
    print(valor_de_lote(products))                # 126.0
    print(producto_maximo_valor(products))        # "P002 - Cuaderno: $62.5"
