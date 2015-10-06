'''Serie trigonometrica de Fourier con python'''
import math


'''variables de control'''
limInf = -math.pi
limSup = math.pi
rectangulos = 20
periodo = limSup - limInf
omega = (2*math.pi) / periodo


'''Funcion de prueba'''
def f(x):
    return x**2


'''Funciones de los ceoficientes a0, an y bn, por el metodo de los rectangulos
arg[0] = funcion
arg[1] = limite inf
arg[2] = limite sup
arg[3] = num de rectangulos
'''

'''coeficiente a0'''
def int_coef_a0(fun, lInf, lSup, numRect):
    deltaX = (lSup - lInf) / float(numRect)
    inte = (fun(lInf) + fun(lSup)) / 2.0
    k = 1
    while k < numRect:
        inte += fun(lInf + k*deltaX)
        k += 1
    return 2*(inte * deltaX)/periodo


'''coeficiente an'''
def int_coef_an(fun, lInf, lSup, numRect):
    deltaX = (lSup - lInf) / float(numRect)
    inte = ((fun(lInf)*math.cos(omega*lInf)) + (fun(lSup)*math.cos(omega*lSup))) / 2.0
    k = 1
    while k < numRect:
        inte += fun(lInf + k*deltaX)*math.cos(omega*(lInf + k*deltaX))
        k += 1
    return 2*(inte * deltaX)/periodo


'''coeficiente bn'''
def int_coef_bn(fun, lInf, lSup, numRect):
    deltaX = (lSup - lInf) / float(numRect)
    inte = ((fun(lInf)*math.sin(omega*lInf)) + (fun(lSup)*math.sin(omega*lSup))) / 2.0
    k = 1
    while k < numRect:
        inte += fun(lInf + k*deltaX)*math.sin(omega*(lInf + k*deltaX))
        k += 1
    return 2*(inte * deltaX)/periodo


'''Impresion de los resultado aproximados'''
print 'Los resultados aproximados de los coeficientes a0, an y bn son:'
print 'a0 = ', int_coef_a0(f, limInf, limSup, rectangulos)
print 'an = ', int_coef_an(f, limInf, limSup, rectangulos)
print 'bn = ', int_coef_bn(f, limInf, limSup, rectangulos)
