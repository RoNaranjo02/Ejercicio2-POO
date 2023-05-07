from claseViajeroF import Viajero
import csv

class ManejadorV:
    __lista = []
    def __init__(self):
         self.__lista = []
         
    def readFile(self):
        archivo = open("viajerosFrecuentes.csv")
        reader = csv.reader (archivo, delimiter=',')
        for fila in reader:
            viajerosN = Viajero(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__lista.append(viajerosN)
        archivo.close()
    
    def busqpersona(self, usuario):
        flag = False
        i = 0
        while ((i<= len(self.__lista)) & (flag == False)):
            if self.__lista[i].getnumviajero() == usuario:
                flag = True
                j = i
            i+=1
        if flag == False:
            print("El numero de pasajero no es correcto")
        elif flag == True:
            return (j)
    
    def MostrarMillas(self, j):
        return self.__lista[j].getMillas()
    
    def millas_Acum(self, j, acum):
        self.__lista[j].acumularMillas(acum)
        

        
        
#def canjearMillas(self, cMillas):
        #if cMillas <= self.__millas:
            
            #elif: print("Error en la operacion.")
    #def busqViajero(self, usuario, lista):
