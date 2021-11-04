import math

def rincontr(x0,Cg):
	error = -999
	t = 1.5708 - 3*x0
	while(error!=0):
		fx = ((2*math.cos(t)*(1+math.sin(x0)))/(1-math.sin(t-x0)))-1-Cg
		fprima = (2*math.cos(x0)*math.sin(3*x0))/(1-math.sin(4*x0))+(6*(math.sin(x0)+1)*math.cos(3*x0))/(1-math.sin(4*x0))+(8*(math.sin(x0)+1)*math.sin(3*x0)*math.cos(4*x0))/math.pow((1-math.sin(4*x0)),2)
		x = x0-fx/fprima
		print(x)
		error = abs(x-x0)
		x0 = x

	return x0


x0 = float(input('Ingrese el valor inicial theta [rad]: '))
Cg = float(input('ingrese la concentración solar: '))

thetatr = rincontr(x0,Cg)
print(thetatr)

	


