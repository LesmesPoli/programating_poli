import json
import os

# Asegurar que se abra desde la carpeta del script
base_path = os.path.dirname(__file__)
with open(os.path.join(base_path, "productos.json"), "r", encoding="utf-8") as f:
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
            print(f"✅ Producto agregado: {producto['nombre']} x{cantidad}")
        else:
            print("⚠️ No tenemos tanto producto, revise la lista.")
            return False
    else:
        print("⚠️ Producto no válido.")
        return False
    return True

def confirmar_compra():
    print("\n--- Resumen de Compra ---")
    if not carrito:
        print("Carrito vacío, no se realizó ninguna compra.")
        return
    total = 0
    for item in carrito:
        print(f"{item['nombre']} x{item['cantidad']} = {item['subtotal']}")
        total += item['subtotal']
    print(f"\nTotal a pagar: {total}")

if __name__ == "__main__":
    while True:
        mostrar_productos()
        try:
            indice = int(input("\nIngrese el número del producto que desea comprar: "))
            cantidad = int(input("Ingrese la cantidad: "))
            exito = agregar_producto(indice, cantidad)

            # Si no se pudo agregar, preguntar si quiere intentar de nuevo
            if not exito:
                continuar = input("¿Desea intentar con otro producto? (s/n): ").lower()
                if continuar != "s":
                    break
                else:
                    continue

            continuar = input("¿Desea agregar otro producto al carrito? (s/n): ").lower()
            if continuar != "s":
                break
        except ValueError:
            print("⚠️ Entrada inválida, intente de nuevo.")

    confirmar_compra()
