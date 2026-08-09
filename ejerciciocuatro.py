# Programa para calcular una factura con 10 productos

producto1 = float(input("Ingrese el valor del producto 1: "))
producto2 = float(input("Ingrese el valor del producto 2: "))
producto3 = float(input("Ingrese el valor del producto 3: "))
producto4 = float(input("Ingrese el valor del producto 4: "))
producto5 = float(input("Ingrese el valor del producto 5: "))
producto6 = float(input("Ingrese el valor del producto 6: "))
producto7 = float(input("Ingrese el valor del producto 7: "))
producto8 = float(input("Ingrese el valor del producto 8: "))
producto9 = float(input("Ingrese el valor del producto 9: "))
producto10 = float(input("Ingrese el valor del producto 10: "))

# Calcular el subtotal
subtotal = (producto1 + producto2 + producto3 + producto4 + producto5 +
            producto6 + producto7 + producto8 + producto9 + producto10)

# Calcular el IVA (19%)
iva = subtotal * 0.19

# Calcular el total
total = subtotal + iva

# Mostrar resultados
print("\n------ FACTURA ------")
print("Subtotal: $", subtotal)
print("IVA (19%): $", iva)
print("Total a pagar: $", total)
print("Mi primer programa en Python")
print("verifico factura")






