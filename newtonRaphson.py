import math 


x0 = float(input('Ingrese el valor inicial x0: '))
error = -999

while(error!=0):
	fx = pow(x0,3)-1.3761 * pow(x0,2)-254738.59
	fprima = 3*pow(x0,2)-2.7522*x0
	x = x0- (fx/fprima)
	error = abs(x-x0)
	x0 = x

print(x0)

