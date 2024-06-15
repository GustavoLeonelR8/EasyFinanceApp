import tkinter as tk
from tkinter import messagebox

class EasyFinanceApp:
    def __init__(self):
        self.tipo_cambio = 36.66  # Tipo de cambio dólar-córdoba
        self.gastos = []
        self.ingresos = []

        # Configuración de la ventana principal
        self.root = tk.Tk()
        self.root.title("EasyFinanceApp")
        self.root.geometry("400x400")
        
        # Menú principal
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(expand=True)

        self.label = tk.Label(self.menu_frame, text="¡Bienvenido a EasyFinanceApp!", font=("Arial", 16))
        self.label.pack(pady=10)
        
        self.convert_button = tk.Button(self.menu_frame, text="Convertir moneda local a dólares", command=self.mostrar_convertir_a_dolares, width=25, height=2)
        self.convert_button.pack(pady=5)
        
        self.gasto_button = tk.Button(self.menu_frame, text="Registrar un gasto", command=self.mostrar_registrar_gasto, width=25, height=2)
        self.gasto_button.pack(pady=5)
        
        self.ingreso_button = tk.Button(self.menu_frame, text="Registrar un ingreso", command=self.mostrar_registrar_ingreso, width=25, height=2)
        self.ingreso_button.pack(pady=5)
        
        self.estado_button = tk.Button(self.menu_frame, text="Ver estado de cuenta", command=self.ver_estado_cuenta, width=25, height=2)
        self.estado_button.pack(pady=5)
        
        self.salir_button = tk.Button(self.menu_frame, text="Salir", command=self.root.quit, width=25, height=2)
        self.salir_button.pack(pady=5)

        # Frame para las operaciones
        self.operation_frame = tk.Frame(self.root)
        
        # Entry y Labels para las operaciones
        self.operation_label = tk.Label(self.operation_frame)
        self.operation_entry1 = tk.Entry(self.operation_frame)
        self.operation_entry2 = tk.Entry(self.operation_frame)
        self.submit_button = tk.Button(self.operation_frame, text="Submit", command=self.submit_operation)
        
    def mostrar_convertir_a_dolares(self):
        self.clear_operation_frame()
        self.operation_label.config(text="Ingrese el monto en moneda local:")
        self.operation_label.pack(pady=10)
        self.operation_entry1.pack(pady=5)
        self.submit_button.pack(pady=10)
        self.submit_button.config(command=self.convertir_a_dolares)
        self.operation_frame.pack(pady=20)
        
    def mostrar_registrar_gasto(self):
        self.clear_operation_frame()
        self.operation_label.config(text="Ingrese la descripción del gasto:")
        self.operation_label.pack(pady=10)
        self.operation_entry1.pack(pady=5)
        self.operation_entry1.delete(0, tk.END)
        self.operation_entry2.pack(pady=5)
        self.operation_entry2.delete(0, tk.END)
        self.operation_entry2.insert(0, "Ingrese el monto del gasto")
        self.operation_entry2.bind("<FocusIn>", self.clear_placeholder)
        self.submit_button.pack(pady=10)
        self.submit_button.config(command=self.registrar_gasto)
        self.operation_frame.pack(pady=20)
        
    def mostrar_registrar_ingreso(self):
        self.clear_operation_frame()
        self.operation_label.config(text="Ingrese la descripción del ingreso:")
        self.operation_label.pack(pady=10)
        self.operation_entry1.pack(pady=5)
        self.operation_entry1.delete(0, tk.END)
        self.operation_entry2.pack(pady=5)
        self.operation_entry2.delete(0, tk.END)
        self.operation_entry2.insert(0, "Ingrese el monto del ingreso")
        self.operation_entry2.bind("<FocusIn>", self.clear_placeholder)
        self.submit_button.pack(pady=10)
        self.submit_button.config(command=self.registrar_ingreso)
        self.operation_frame.pack(pady=20)
        
    def clear_operation_frame(self):
        for widget in self.operation_frame.winfo_children():
            widget.pack_forget()
        self.operation_frame.pack_forget()
        
    def clear_placeholder(self, event):
        if event.widget.get() in ["Ingrese el monto del gasto", "Ingrese el monto del ingreso"]:
            event.widget.delete(0, tk.END)

    def convertir_a_dolares(self):
        try:
            monto_local = float(self.operation_entry1.get().replace(",", ""))
            monto_dolares = monto_local / self.tipo_cambio
            messagebox.showinfo("Conversión a Dólares", f"El monto en dólares es: ${monto_dolares:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
        
    def registrar_gasto(self):
        descripcion = self.operation_entry1.get()
        try:
            monto = float(self.operation_entry2.get().replace(",", ""))
            self.gastos.append({'descripcion': descripcion, 'monto': monto})
            messagebox.showinfo("Registrar Gasto", f"Gasto registrado con éxito: {descripcion} - C${monto:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido para el monto.")
        
    def registrar_ingreso(self):
        descripcion = self.operation_entry1.get()
        try:
            monto = float(self.operation_entry2.get().replace(",", ""))
            self.ingresos.append({'descripcion': descripcion, 'monto': monto})
            messagebox.showinfo("Registrar Ingreso", f"Ingreso registrado con éxito: {descripcion} - C${monto:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido para el monto.")
        
    def ver_estado_cuenta(self):
        total_gastos = sum(gasto['monto'] for gasto in self.gastos)
        total_ingresos = sum(ingreso['monto'] for ingreso in self.ingresos)
        balance = total_ingresos - total_gastos
        
        estado = (
            f"Estado de cuenta:\n\n"
            f"Total de gastos: C${total_gastos:.2f}\n"
            f"Total de ingresos: C${total_ingresos:.2f}\n"
            f"Balance: C${balance:.2f}"
        )
        
        messagebox.showinfo("Estado de Cuenta", estado)
    
    def submit_operation(self):
        pass  # Se define en cada método para realizar la operación correspondiente.

    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = EasyFinanceApp()
    app.ejecutar()
