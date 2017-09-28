"""Funcion que imprime las tablas de multiplicar del uno al 10"""
'''Santana Mares Jasmin Aide GITI9071'''
def tablas():
    for i in range(1,11):
        for j in range(1,11):
            print (str(i) +"*"+str(j)+"="+str (i*j))
