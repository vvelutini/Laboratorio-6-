import modelos_biblioteca

# Base de datos en memoria
inventario = {}
categorias = set()
usuarios = {}

# 1) agregar_categoria
categorias = modelos_biblioteca.agregar_categoria(categorias, "Fantasía")
categorias = modelos_biblioteca.agregar_categoria(categorias, "Fantasía")  # duplicado, no se repite
print("Categorías:", categorias)

# 2) registrar_libro
inventario, categorias = modelos_biblioteca.registrar_libro(inventario, "111", "El Hobbit", "J.R.R. Tolkien", "Fantasía", categorias)
inventario, categorias = modelos_biblioteca.registrar_libro(inventario, "222", "Dune", "Frank Herbert", "Ciencia Ficción", categorias)
inventario, categorias = modelos_biblioteca.registrar_libro(inventario, "333", "Sapiens", "Yuval Noah Harari", "Historia", categorias)
print("Inventario:", inventario)
print("Categorías:", categorias)

# 3) registrar_usuario
usuarios = modelos_biblioteca.registrar_usuario(usuarios, "u1", "Ana")
usuarios = modelos_biblioteca.registrar_usuario(usuarios, "u2", "Luis")
print("Usuarios:", usuarios)

# 4) prestar_libro
usuarios = modelos_biblioteca.prestar_libro("111", "u1", inventario, usuarios)
print("Usuarios después del préstamo:", usuarios)
print("Inventario después del préstamo:", inventario)

# Casos donde no se puede prestar
usuarios = modelos_biblioteca.prestar_libro("999", "u1", inventario, usuarios)  # libro no existe
usuarios = modelos_biblioteca.prestar_libro("222", "u3", inventario, usuarios)  # usuario no existe
