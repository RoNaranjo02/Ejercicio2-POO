import math

class Viajero:
    __num_viajero = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = ""
    
    def __init__(self,num_viajero="",dni="",nombre="",apellido="",millas_acum=""):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido =apellido
        self.__millas_acum = millas_acum
    
    def __str__(self):
        return 'Numero de viajero: {} Dni: {} Nombre: {} Apellido: {} Millas acumuladas: {}'.format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    
    def geDni(self):
        return self.__dni
    
    def getApellido(self):
        return self.__apellido
    
    def getMillas(self):
        return self.__millas_acum
    
    def getnumviajero(self):
        return self.__num_viajero
    
    def getnombre(self):   
        return self.__nombre
    
    def acumularMillas(self, acum):
        self.__millas_acum = self.__millas_acum + acum
        
    
         

