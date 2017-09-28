"""Se ingresa un usuario y una contraseña si son las correctas manda un mensaje de Binevenida"""
'''Santana Mares Jasmin Aide GITI9071'''
def login():
    user =input ("User: ")
    password = input("Password: ")
    if (user=='utng' and password == 'mexico'):
        return 'Bienvenido'
