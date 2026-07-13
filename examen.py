juegos=[]

def menu():
    print("---Menu principal---")
    print("1.-Stock por plataforma")
    print("2.-Busqueda de juegos por rango de precio")
    print("3.-Actualizar precio de juego")
    print("4.-Agregar juego")
    print("5.-Eliminar juego")
    print("6.-Salir")
#separacion
def stock_plataforma():
    nombre_plataforma = input("Ingrese el nombre de la plataforma: ").strip()
    encontrados = [j for j in juegos if j["plataforma"].lower() == nombre_plataforma.lower()]
    if not encontrados:
        print("No se encontraron juegos para esa plataforma")
        return
    for juego in encontrados:
        print(f"Titulo: {juego['titulo']} - Stock: {juego['stock']}")
#separacion 
def busqueda_juegos():
    try:
        precio_min = int(input("Ingrese el precio minimo: "))
        precio_max = int(input("Ingrese el precio maximo: "))
    except ValueError:
        print("Ingrese valores numericos validos")
        return
    encontrados = [j for j in juegos if precio_min <= j["precio"] <= precio_max]
    if not encontrados:
        print("No se han encontrado juegos dentro de sus criterios")
        return
    for juego in encontrados:
        print(f"Titulo: {juego['titulo']} - Precio: {juego['precio']} - Plataforma: {juego['plataforma']}")
#separacion
def actualizar_precio_juego():
    nombre_juego = input("Ingrese el nombre del juego: ").strip()
    try:
        precio_nuevo = int(input("Ingrese el nuevo precio: "))
    except ValueError:
        print("Ingrese un precio valido")
        return
    for juego in juegos:
        if juego["titulo"].lower() == nombre_juego.lower():
            juego["precio"] = precio_nuevo
            print(f"Precio actualizado para {juego['titulo']}")
            return
    print("Juego no encontrado")
#separacion
def agregar_juego():
    titulo = input("Ingrese el nombre del juego: ").strip()
    plataforma = input("Ingrese la plataforma del juego: ").strip()
    genero = input("Ingrese el genero del juego: ").strip()
    clasificacion = input("Ingrese la clasificacion del juego: ").strip().lower()
    multiplayer_opcion = input("Ingrese si el juego posee multijugador (S or N): ").strip().lower()
    multiplayer = multiplayer_opcion == "s"
    editor = input("Ingrese el editor del juego: ").strip()
    try:
        precio = int(input("Ingrese el precio del juego: "))
        stock = int(input("Ingrese el stock del producto: "))
    except ValueError:
        print("Ingrese valores numericos validos")
        return
    if precio < 0 or stock < 0:
        print("Por favor ingrese valores mayores o iguales a 0")
        return
    juego = {
        "titulo": titulo,
        "plataforma": plataforma,
        "genero": genero,
        "clasificacion": clasificacion,
        "multiplayer": multiplayer,
        "editor": editor,
        "precio": precio,
        "stock": stock,
    }
    juegos.append(juego)
    print(f"Juego {titulo} agregado correctamente")
#separacion
def eliminar_juego():
    juego_eliminado = input("Ingrese el juego a eliminar: ").strip()
    for indice, juego in enumerate(juegos):
        if juego["titulo"].lower() == juego_eliminado.lower():
            juegos.pop(indice)
            print(f"Juego {juego_eliminado} eliminado correctamente")
            return
    print("Juego no encontrado")
#separacion
def salir():
    print("Saliendo del programa")
#separacion
def main():
    while True:
        menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion valida")
            continue
        if opcion == 1:
            stock_plataforma()
        elif opcion == 2:
            busqueda_juegos()
        elif opcion == 3:
            actualizar_precio_juego()
        elif opcion == 4:
            agregar_juego()
        elif opcion == 5:
            eliminar_juego()
        elif opcion == 6:
            salir()
            break
        else:
            print("Ingrese una opcion valida")
main()
