import math

theta0 = float(input('Ingrese el valor de theta cero [rad]: '))
thetaR = float(input('Ingrese el valor inicial de theta r [rad]: '))
salto = float(input('Ingrese el valor del salto para calcular theta r [rad]: '))
CgMax = -10

while (thetaR<=1.5708):

	Cg = (((math.sin(thetaR)*math.cos(thetaR+theta0))/math.sin(theta0))-1) * ((2*(1+math.sin(thetaR + theta0))*math.sin(3*(thetaR + theta0)))/(1-math.cos(4*(thetaR+theta0))))
	print(Cg,thetaR)
	if (Cg > CgMax):
		CgMax = Cg
		thetaR += salto
	if (Cg<CgMax):
		print('\n\tLa concentración máxima es: ',CgMax)
		thetaR = math.degrees(thetaR)
		print('\tEl valor de theta r es de ',thetaR)
		break
