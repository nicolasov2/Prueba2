#Codigo solucion

def imprimir_lista(**kwargs): # **kwargs es un diccionario
    for key, value in kwargs.items(): #key es la llave y value es el valor
        print(key, value.upper()) # Imprime la llave y el valor en mayusculas

def main():
    Lista = {} # Diccionario vacio
    print("Para terminar de ingresar colores, digite: 'SALIR'") # Mensaje de ayuda
    while True: #Ciclo de ingreso de datos hasta que se ingrese SALIR
        color_fav = input("Ingresa tu color favorito: ") 
        if color_fav == "salir" or color_fav == "Salir" or color_fav == "SALIR": # Si el usuario ingresa "salir,Salir o SALIR" se termina el ciclo
            break
        else: # Si el usuario no ingresa salir, se agrega el color a la lista
            Lista[color_fav] = color_fav # Se agrega el color a la lista
    imprimir_lista(**Lista) # Se imprime la lista

if __name__ == '__main__':
    main()
    
    
# •	Ejercicio 5 (18 puntos):
# Pregunte al usuario sus colores favoritos, cuando el usuario ingrese "salir" el programa debe terminar de pedir sus colores favoritos. Cree una función que imprima en mayúsculas los colores, uno por linea. Utilice kwargs o args según corresponda.
