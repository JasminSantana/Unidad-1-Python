""" Convierte de grados fahrenheit​ ​a Celsius​ ​y​ ​viceversa​,
indicando el tipo de grados y la cantidad """
''' Autor:Santana Mares Jasmin Aide
Grupo:GTI9071'''
def conversion():
    tipoConversion= input("write the degree conversion type Celsius or Fahrenheit: ")
    grados= int (input("Write the grades: "))
    if (tipoConversion == 'celsius'):
        fahrenheit= (grados * 1.8) + 32
        return 'Grades Fahrenheit '+ str(fahrenheit)
    if tipoConversion == 'fahrenheit':
        celsius= (grados - 32) / 1.8
        return 'Grades Celsius = '+ str(celsius)
