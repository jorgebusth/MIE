'''Este programa sirve para dimensionar un calentador solar'''

import math
import calorLatente

# Cálculo del flujo de aire necesario para el secad0



Tboil = float(input('\n\nIngrese la temperatura de ebullición: '))
Tcold = float(input('Ingrese la temperatura de congelación: '))
Icolector = float(input('Ingrese la radiación incidente promedio sobre el plano del colector [W/m^2]: '))
deltaT = 2*0.25*(Tboil-Tcold)*(Icolector/1367)


# Cantidad de agua que se debe extraer del producto

Ww = float(input('Ingrese la masa inicial [kg]: '))
Miwb = float(input('Ingrese la humedad inicial base húmeda del producto: '))
Mfwb = float(input('Ingrese la humedad final del producto base húmeda: '))
Mw = ((Miwb-Mfwb)*Ww)/(1-Mfwb) #cantidad de agua que se debe extraer del producto.

# El volumen de aire seco que debe pasar por la cámara de aire

Ra = 283 # constante de los gases ideales kJ/kgK
Pa = 101.325 # presión parcial del aire seco en la atmósfera [Pa]
Cpa = 1.012 # calor específico del aire a presión constante [kJ/kgK]
Ta = float(input('Ingrese la temperatura ambiente [ºC]: '))
Ta = Ta + 273.15
Tf = Ta+0.25*deltaT
To = Ta+deltaT # temperatura del secador a la salida de aire del colector.
Tpt = 0.25*(3*To+Ta)

Lt = calorLatente.calorL(Tpt)
Lt = Lt/1000000


Va = (Mw*Lt*Ra*Ta)/(Cpa*Pa*(To-Tf))

# Después de calcular el volumen de aire seco se obtiene el flujo de aire. Lam. 9
t = 8 # tiempo de secado encontrado experimentalmente
G = Va / t


# Área del interior de la cámara .
print('\n\n\tCálculo del área interior\n')
rho = float(input('Ingrese la densidad del producto en condiciones húmedas: '))
hl = 0.01
xi = float(input('Ingrese la porosidad del producto: '))
epsilonv = 0.3

A = Ww / (rho*hl*xi*(1-epsilonv))

# Cálculo de la densidad de carga de las charolas del colector lam. 11

L = rho * hl * xi * (1 - epsilonv)

# Se calcula el área del colector.
print('\n\n\tSe determina el área de captación\n')
eta = float(input('Ingrese la eficiencia del sistema de secado: '))
It = 1100
Ac = ((Mw/28800) * (Lt*1000000)) / (It * eta)


# se imprimen los resultados
print('\n\n\tRESULTADOS\n')
print('La diferencia de temperatura que sale del colector y la temperatura ambiente es de {:.2f}'.format(deltaT))
print('La cantidad de agua que se debe extraer al producto para llevarlo a la humedad final es {:.2f} kg.'.format(Mw))
print('El calor latente es {:.2f} MJ/kg'.format(Lt))
print('Volumen de aire seco necesario es {:.2f} m^3'.format(Va))
print('El flujo de aire requerido es de {:.2f}m³/h'.format(G))
print('El área interna de la cámara de secado es de {:.2f} m²'.format(A))
print('La densidad de carga de las bandejas es {:.2f} m²'.format(L))
print('El aréa de captación es de {:.4f} m²\n\n'.format(Ac))