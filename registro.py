import pickle
from getpass import getpass


class NuevoUsuario ():
    def __init__(self, usuario, contraseña, nombre):
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = nombre
        self.usermode = 1

    def reg(self):
        print("Hola", self.nombre, ", te has registrado correctamente.\nLoguea con '",
              self.usuario, "' para continuar")

    def log(self):
        print("Hola", self.nombre,
              ", si hubiese algo mas en el programa podrias continuar.")

    def admin(self):
        self.usermode = 2
        print("El Usuario", self.usuario, "esta registrado como ADMIN")


user_mode = 0


def login():
    global user_mode
    user = input("introduce usuario:\n")
    psw = getpass("introduce contraseña:\n")
    try:
        file = open(user+".usr", "rb")
        user_in_l = pickle.load(file)
        if user_in_l.contraseña == psw:
            user_in_l.log()
            user_mode = user_in_l.usermode
            file.close()
            del file
        else:
            print("usuario o contraseña incorrecta")
    except FileNotFoundError:
        print("usuario o contraseña incorrecta")


def logout():
    global main_menu
    global user_mode
    print("hasta luego")
    user_mode = 0
    main_menu = (None)


def registro():
    global main_menu
    user = input("Introduce usuario:\n")
    # Admin
    if user == ("##ADMIN##"):
        print("~~~CREANDO CUENTA ADMIN~~~")
        user = input("Introduce usuario:\n")
        try:
            file = open(user+".usr", "rb")
            print("El usuario ya existe")
            file.close()
            del file
            main_menu = (None)
        except FileNotFoundError:
            psw = getpass("introduce contraseña:\n")
            psw_2 = getpass("Repite contraseña:\n")
            if psw == psw_2:
                nom = input("introduce nombre:\n")
                in_user = NuevoUsuario(user, psw, nom)
                in_user.admin()
                user_list = [user, nom, in_user.usermode]
                with open(user+".usr", "wb")as file:
                    pickle.dump(in_user, file)
                with open("alluser.txt", "a")as file_1:
                    file_1.writelines(
                        '#~' + user_list[0] + '-' + user_list[1] + '\n')
            else:
                print("Las contraseñas no coinciden")
    # Usuario
    else:
        try:
            file = open(user+".usr", "rb")
            print("El usuario ya existe")
            file.close()
            del file
            main_menu = (None)
        except FileNotFoundError:
            psw = getpass("introduce contraseña:\n")
            psw_2 = getpass("Repite contraseña:\n")
            if psw == psw_2:
                nom = input("introduce nombre:\n")
                in_user = NuevoUsuario(user, psw, nom)
                in_user.reg()
                user_list = [user, nom, in_user.usermode]
                with open(user+".usr", "wb")as file:
                    pickle.dump(in_user, file)
                with open("alluser.txt", "a")as file_1:
                    file_1.writelines(user_list[0] + '-' + user_list[1] + '\n')
            else:
                print("Las contraseñas no coinciden")


def eliminar():
    pass


main_menu = int(input("1-Login\n2-Registro\n0-salir\n"))
while True:
    if main_menu == 1 and user_mode == 0:
        login()
    elif main_menu == 1 and user_mode >= 1:
        logout()
    elif main_menu == 2:
        registro()
    elif main_menu == 3:
        with open("alluser.txt", "r") as file_1:
            lista_completa = file_1.readlines()
        for i in (lista_completa):
            print(i.strip())
    elif main_menu == 0:
        break
    else:
        print("Capullo")
    if user_mode == 0:
        main_menu = int(
            input("1-Login\n2-Registro\n0-salir\n"))
    elif user_mode == 1:
        main_menu = int(
            input("1-Log out\n2-Editar\n3-Eliminar cuenta\n0-salir\n"))
    elif user_mode == 2:
        main_menu = int(
            input("1-Log out\n2-Editar\n3-Eliminar cuenta\n4-ADMINISTRAR CUENTAS\n0-salir\n"))
