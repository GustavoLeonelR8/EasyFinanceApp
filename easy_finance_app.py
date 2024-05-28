class EasyFinanceApp:
    def __init__(self):
        self.tipo_cambio = 36.66  # Tipo de cambio dólar-córdoba
        self.gastos = []
        self.ingresos = []

    def mostrar_menu(self):
        print("\n¡Bienvenido a EasyFinanceApp!")
        print("Por favor, seleccione una opción:")
        print("1. Convertir moneda local a dólares.")
        print("2. Registrar un gasto.")
        print("3. Registrar un ingreso.")
        print("4. Ver estado de cuenta.")
        print("5. Salir.")

    def convertir_a_dolares(self):
        monto_local = float(input("Ingrese el monto en moneda local: "))
        monto_dolares = monto_local / self.tipo_cambio
        print("El monto en dólares es: $" + str(monto_dolares))

    def registrar_gasto(self):
        descripcion = input("Ingrese la descripción del gasto: ")
        monto = float(input("Ingrese el monto del gasto: "))
        self.gastos.append({'descripcion': descripcion, 'monto': monto})
        print("Gasto registrado con éxito.")

    def registrar_ingreso(self):
        descripcion = input("Ingrese la descripción del ingreso: ")
        monto = float(input("Ingrese el monto del ingreso: "))
        self.ingresos.append({'descripcion': descripcion, 'monto': monto})
        print("Ingreso registrado con éxito.")

    def ver_estado_cuenta(self):
        total_gastos = sum(gasto['monto'] for gasto in self.gastos)
        total_ingresos = sum(ingreso['monto'] for ingreso in self.ingresos)
        balance = total_ingresos - total_gastos

        print("\nEstado de cuenta:")
        print(f"Total de gastos: ${total_gastos}")
        print(f"Total de ingresos: ${total_ingresos}")
        print(f"Balance: ${balance}")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese su opción: ")

            if opcion == '1':
                self.convertir_a_dolares()
            elif opcion == '2':
                self.registrar_gasto()
            elif opcion == '3':
                self.registrar_ingreso()
            elif opcion == '4':
                self.ver_estado_cuenta()
            elif opcion == '5':
                print("Gracias por usar EasyFinanceApp. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    app = EasyFinanceApp()
    app.ejecutar()
