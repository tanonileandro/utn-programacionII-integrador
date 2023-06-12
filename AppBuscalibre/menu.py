from conexion import ConexionSQLite
from buscaLibre import BuscaLibre


def mostrar_menu():
    print(" BUSCALIBRE MENU ".center(60, '-'))
    print("1- Cargar Libros")
    print("2- Modificar precio de un libro")
    print("3- Borrar un libro")
    print("4- Cargar disponibilidad")
    print("5- Listado de Libros")
    print("6- Ventas")
    print("7- Actualizar Precios")
    print("8- Mostrar registros anteriores a una fecha en específico")
    print("9- Mostrar historial de libros")
    print("10- Mostrar historial de ventas")
    print("0- Salir del menú")
    print('-' * 60)


def ejecutar_menu():
    conexion = ConexionSQLite("buscalibre.db")
    conexion.conectar()

    buscalibre = BuscaLibre(conexion)

    buscalibre.crear_tabla_libros()
    buscalibre.crear_tabla_ventas()
    buscalibre.crear_tabla_historico_libros()

    opcion = None

    while opcion != "0":
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            buscalibre.cargar_libros()
        elif opcion == "2":
            buscalibre.modificar_precio_libro()
        elif opcion == "3":
            buscalibre.borrar_libro()
        elif opcion == "4":
            buscalibre.cargar_disponibilidad()
        elif opcion == "5":
            buscalibre.listar_libros()
        elif opcion == "6":
            buscalibre.realizar_venta()
        elif opcion == "7":
            buscalibre.actualizar_precios()
        elif opcion == "8":
            buscalibre.mostrar_registros_anteriores_fecha()
        elif opcion == "9":
            buscalibre.mostrar_historico_libros()
        elif opcion == "10":
            buscalibre.mostrar_ventas()
        elif opcion == "0":
            print("Saliendo del menú...")
        else:
            print("Opción inválida. Intente nuevamente.")

    conexion.desconectar()


if __name__ == "__main__":
    ejecutar_menu()