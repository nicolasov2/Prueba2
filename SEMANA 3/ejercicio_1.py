def leer_correos():
    archivo = open("correos.txt", "r")
    correos = []
    for linea in archivo:
        correos.append(linea.strip())
    archivo.close()
    return correos

def buscar_correo(correos):
    correo = input("Ingrese el correo a buscar: ")
    if correo in correos:
        print("------------------------------------")
        print("El correo se encuentra en la lista")
        posicion = correos.index(correo) + 1
        print("\nLa posicion del correo es: ", posicion )
        print("El proveedor del correo es: ", correo.split(".")[0])
        print("------------------------------------")
    else:
        print("El correo no se encuentra en la lista")
        print ("-1")

def buscar_proveedor(correos):
    proveedor = input("\nIngrese el proveedor a buscar: ")
    print("------------------------------------\n")
    for correo in correos:
        if proveedor in correo.split(".")[0]:
            print(correo + "| de la posicion : " + str(correos.index(correo) + 1))

def main():
    correos = leer_correos()
    print("\nLa cantidad de correos es: ", len(correos))
    buscar_correo(correos)
    buscar_proveedor(correos)

if __name__ == '__main__':
    main()
