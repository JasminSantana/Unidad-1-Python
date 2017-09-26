"""  Calcula el resultado de la operacion dados dos numeros """
'''Autor: Santana Mares Jasmin Aide
Grupo: GTI9071'''
def conversion():
    num1= int(input("Write the first number : "))
    num2= int(input("Write the second number : "))
    operacion= input("Write the operation : ")
    if(operacion  in "suma"):
        return 'La suma es = '+ str(num1 + num2)
    if(operacion in "resta"):
        return 'La resta es = '+ str(num1 - num2)
    if(operacion in "multiplicacion"):
        return 'La multiplicación es = '+str(num1 * num2)
    if(operacion in "division"):
        return 'La división es = '+str(num1 / num2)
