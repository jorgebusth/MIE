import math
Qe = 43500
P1= 102.4
T1 = 294
ui1 = 209.77
Vr1 = 653.54
rc = float(input('Ingrese la relación de compresión:'))

# para obtener el estado 2

Vr2 = Vr1/rc
print('Vr2=',Vr2)
T2 = float(input('Ingrese el valor correspondiente de temperatura del volumen relativo 2 [K]:'))
ui2 = float(input('Con el mismo valor ingrese la energía interna 2 correspondiente [kJ/kg]:'))
P2 = P1*(T2/T1)*rc

# para el estado 3

ui3 = Qe+ui2
T3 = 2200 + ((ui3-1872.4)/(1921.3-1872.4))*(2250-2200)
P3 = P2 * (T3/T2)
Vr3 = 2.012+((ui3-1872.4)/(1921.3-1872.4))*(1.864-2.012)
if(Vr3<0):
	Vr3 = 1

if(Vr3 == 1):
	Vr4 = rc
else:
	Vr4 = Vr3*rc
print('Vr4=',Vr4)

T4 = float(input('Para la temperatura 4 busque en tablas el valor que corresponde a Vr4:'))
ui4 = float(input('De acuerdo a las tablas con el valor del volumen relativo del estado 4 ingrese el valor de la energía interna:'))
P4 = P3 * (T4/T3)*(Vr4/Vr3)
Qs = ui4-ui1
Wn = Qe - Qs
eta = Wn / Qe
etaReal = (0.4 * eta)*100
# resumen de los estados termodinámicos
print('\n\t\t Estados termodinámicos\n')
print('\t Estado 1\n\n\t Presión:',P1,'kPa\n\t Temperatura:',T1,'K\n\t Energía interna:',ui1,'kJ/kg\n\t Volumen relativo:',Vr1)
print('\n\t Estado 2\n\n\t Presión:',P2,'kPa\n\t Temperatura:',T2,'K\n\t Energía interna:',ui2,'kJ/kg\n\t Volumen relativo:',Vr2)
print('\n\t Estado 3\n\n\t Presión:',P3,'kPa\n\t Temperatura:',T3,'K\n\t Energía interna:',ui3,'kJ/kg\n\t Volumen relativo:',Vr3)
print('\n\t Estado 4\n\n\t Presión:',P4,'kPa\n\t Temperatura:',T4,'K\n\t Energía interna:',ui4,'kJ/kg\n\t Volumen relativo:',Vr4)

print('\n\n\tEl trabajo neto es',Wn,'kJ/kg')
print('La eficiencia térmica real es',etaReal,'%')