#Importamos la libreria reduce.
from functools import reduce

#Creacion de calculadora.
def main():
    List_num = [2,3,4,5,6]  #Lista de numeros.
    Suma = reduce(lambda a,b: a+b,List_num) #Suma de los numeros de la lista.
    Resta = reduce(lambda a,b: a-b,List_num) #Resta de los numeros de la lista.
    Multiplicacion = reduce(lambda a,b: a*b,List_num) #Resta de los numeros de la lista.
    Division = reduce(lambda a,b: a/b,List_num) #Division de los numeros de la lista.
    Exponente = reduce(lambda a,b: a**b,List_num) #Exponente de los numeros de la lista.
    Raiz = reduce(lambda a,b: a**(1/b),List_num) #Raiz de los numeros de la lista.

#Muestra de resultados.
    print("Suma:",Suma,
          "\nResta:",Resta,
          "\nMultiplicacion:",Multiplicacion,
          "\nDivision:",Division,
          "\nExponente:",Exponente,
          "\nRaiz:",Raiz)

if __name__ == '__main__':
    main()
    
    
# •	Ejercicio 3 (18 puntos):
# Cree una calculadora que reciba una lista de numeros. Utilice función lambda, map, filter o reduce según corresponda. 
# Imprima el resultado por la consola.
# Por ejemplo, si la lista es [2, 3, 4, 5, 6], el programa debe devolver:
# Suma: 20
# Resta: -16
# Multiplicación: 720
# División: 0.001388888888888889
# Exponente: 2348542582773833227889480596789337027375682548908319870707290971532209025114608443463698998384768703031934976
# Raiz cuadrada: 1.001927263624698