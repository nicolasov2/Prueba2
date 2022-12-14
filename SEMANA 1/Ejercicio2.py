#Codigo de solución

#Creacion de funcion para determinar si un numero es primo.
def Primo(num):
    for i in range(2, num):
       if num%i==0:
            return False
    return True
#Funcion que determina los numeros primos entre 1 y 1000.
def main():
    Num_primos = list(filter(lambda a: Primo(a),range(1,1001)))
    print(Num_primos)

if __name__ == '__main__':
    main()
    
    
# •	Ejercicio 2 (18 puntos):
# Cree una función que determine si un numero es primo o no. Calcule los numeros primos del 1 al 1000. 
# Solo la función para determinar que es primo puede llevar un for, el resto debe ser con lambda, map, filter o reduce. 
# Imprima la lista por la consola.
