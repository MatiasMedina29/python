Precio=float(input("precio del producto: "))
Cantidad=int(input("cantidad de productos que lleva: "))
Mes=int(input("Numero del mes en que realiza la compra: "))
PrecioTotal=Precio*Cantidad
if Mes==10:
    Desc=PrecioTotal*0.15
    PrecioFinal=PrecioTotal-Desc
    print("Aplica 15% descuento, el precio final es: ", PrecioFinal)
else: print("NO aplica descuento, el precio final es: ", PrecioTotal)