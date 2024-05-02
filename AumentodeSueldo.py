SueldoN1=float(input("Ingrese el sueldo: "))
if SueldoN1<=15.000 and SueldoN1>=0:
    print("Aplica un 20% de aumento", SueldoN1*1.20)
elif SueldoN1<=20.000 and SueldoN1>=15.001:
    print("Aplica un 15% de aumento", SueldoN1*1.10)
elif SueldoN1<=25.000 and SueldoN1>=20.001:
    print("Aplica un 5% de aumento", SueldoN1*1.20)
else: print("No aplica descuento")
