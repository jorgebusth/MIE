''' con esta ecuación se obtiene el calor latente para un secador solar. 
	Lam. 8 clase 17 de calentadores solares.'''
import math
def calorL(Tpt):
	Rg = 461 # constante de los gases para el vapor de agua J/kgK
	Tc = 647.4  # Temperatura crítica del agua K 
	Tb = 373   # Punto de ebullición del agua K
	Pc = 221  # Presión crítica del agua MPa
	Lt = Rg*Tc*Tb*math.log(Pc)*(math.pow((Tc-Tpt),0.38)/ math.pow((Tc-Tb),1.38))
	return Lt


