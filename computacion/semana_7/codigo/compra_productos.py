
import json

# Cargar lista de productos desde el archivo JSON
with open("productos.json", "r", encoding="utf-8") as f:
    productos = json.load(f)

carrito = []

def mostrar_productos():
    print("\n--- Lista de Productos ---")
    for i, p in enumerate(productos, start=1):
        print(f"{i}. {p['nombre']} - Precio: {p['valor']} - Stock: {p['cantidad_disponible']}")

def agregar_producto(indice, cantidad):
    if 1 <= indice <= len(productos):
        producto = productos[indice-1]
        if cantidad <= producto['cantidad_disponible']:
            carrito.append({
                "nombre": producto['nombre'],
                "cantidad": cantidad,
                "valor_unitario": producto['valor'],
                "subtotal": cantidad * producto['valor']
            })
            producto['cantidad_disponible'] -= cantidad
            print(f"Producto agregado: {producto['nombre']} x{cantidad}")
        else:
            print("Error: Stock insuficiente.")
    else:
        print("Producto no válido.")

def confirmar_compra():
    print("\n--- Resumen de Compra ---")
    total = 0
    for item in carrito:
        print(f"{item['nombre']} x{item['cantidad']} = {item['subtotal']}")
        total += item['subtotal']
    print(f"Total a pagar: {total}")
    return total

# Ejemplo de uso interactivo:
if __name__ == "__main__":
    mostrar_productos()
    agregar_producto(1, 2)   # Ejemplo: 2 unidades de Arroz
    agregar_producto(7, 12)  # Ejemplo: 12 unidades de Huevos
    confirmar_compra()
