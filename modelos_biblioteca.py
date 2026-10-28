def agregar_categoria(categorias: set, nueva_categoria: str) -> set:
    """
    Agrega una categoría al conjunto de categorías y devuelve el conjunto actualizado.
    """
    categorias.add(nueva_categoria)
    return categorias


def registrar_libro(inventario: dict, isbn: str, titulo: str, autor: str, categoria: str, categorias: set):
    """
    Crea el libro como una tupla (titulo, autor, categoria), lo guarda en el
    inventario usando el isbn como clave y registra su categoría.
    Devuelve el inventario (dict) y el registro de categorías (set).
    """
    libro = (titulo, autor, categoria)
    inventario[isbn] = libro
    categorias = agregar_categoria(categorias, categoria)
    return inventario, categorias


def registrar_usuario(usuarios: dict, id_usuario: str, nombre) -> dict:
    """
    Guarda al usuario en el diccionario usando su id como clave.
    Cada usuario tiene su nombre y una lista vacía de libros prestados.
    """
    usuarios[id_usuario] = {"nombre": nombre, "libros_prestados": []}
    return usuarios


def prestar_libro(isbn: str, id_usuario: str, inventario: dict, usuarios: dict) -> dict:
    """
    Si el libro y el usuario existen, agrega el isbn a la lista de libros
    prestados del usuario y elimina el libro del inventario.
    Devuelve el registro de usuarios.
    """
    if isbn not in inventario:
        print("El libro con isbn", isbn, "no existe en el inventario")
        return usuarios

    if id_usuario not in usuarios:
        print("El usuario", id_usuario, "no existe")
        return usuarios

    usuarios[id_usuario]["libros_prestados"].append(isbn)
    del inventario[isbn]
    return usuarios
