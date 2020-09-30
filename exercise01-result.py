listaRegistro = []
clientes = 0
costoTotal = 0
pregunta = "" 

while pregunta != "NO": 
    pregunta = input("¿Desea ingresar un nuevo cliente? (SI/NO) ")

    if pregunta == "SI":
        cliente = input("Nombre del cliente: ")
        producto = input("Producto: ")
        costo = float(input("Costo ($0.00): "))
        # registro = {"cliente": cliente, "producto": producto, "costo": costo}
        registro = dict(cliente=cliente, producto=producto, costo=costo)
        # Agregar elemento a la lista
        listaRegistro.append(registro)
        #Total de clientes 
        clientes += 1
        #Sacando los costos totales del día
        costoTotal += float(registro["costo"])

print("Ha dado por finalizado el día.")
print("Reporte: ")
print("El costo total de este día fue de $" + str(costoTotal))
print("Hubo " + str(clientes) + " clientes.")
print("Lista de clientes, productos y costos: ")
for registro in listaRegistro:
    print(registro)

