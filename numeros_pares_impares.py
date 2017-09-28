"""A partir de un número devuelve si es par o impar"""
'''Santana Mares Jasmin Aide GITI9071'''
def par():
    n= int (input("Write a number: "))
    if (n%2==0):
        return "Es par " + str(n)
    else:
         return "Es impar " + str(n)
