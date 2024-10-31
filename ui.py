import tkinter as tk
from tkinter import messagebox
from table_widget import TableWidget
from api_client import APIClient

class EntomologyApp:
    """Encapsula la ventana principal de la aplicación."""

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Entomology Record")
        self.window.geometry("640x600")
        self.window.resizable(False, False)
        self.window.configure(bg="#f5f5dc")

        # Cliente de la API
        self.api_client = APIClient()

        # Tabla de registros
        self.table_widget = TableWidget(self.window)
        self.table_widget.get_frame().pack(expand=True, fill="both", pady=(10, 0))

        # Frame de búsqueda y actualización
        control_frame = tk.Frame(self.window, bg="#f5f5dc")
        control_frame.pack(pady=10)

        # Entrada de texto para el número de insecto
        self.search_entry = tk.Entry(control_frame, width=30)
        self.search_entry.grid(row=0, column=0, padx=5)

        # Botón de búsqueda
        search_button = tk.Button(
            control_frame, text="Buscar Insecto", command=self.search_record
        )
        search_button.grid(row=0, column=1)

        # Botón de actualizar
        refresh_button = tk.Button(
            control_frame, text="Actualizar", command=self.refresh_data
        )
        refresh_button.grid(row=0, column=2, padx=5)

        # Frame para la tabla de detalles del insecto seleccionado
        self.detail_frame = tk.Frame(self.window, bg="#e0ffe0", bd=2, relief="groove")
        self.detail_frame.pack(fill="x", padx=10, pady=10)

        # Tabla de detalles sin scroll y con columnas más delgadas
        self.detail_table = TableWidget(self.detail_frame, slim=True, scroll=False)
        self.detail_table.get_frame().pack(fill="x", padx=10, pady=5)

        # Almacenar los datos cargados
        self.data = []
        self.load_data(self.api_client.get_data())  # Carga inicial de datos

    def load_data(self, data):
        """Carga los datos en la tabla y los almacena."""
        self.data = data
        self.table_widget.load_data(data)

    def search_record(self):
        """Busca un registro por el número de insecto y lo muestra en la tabla de detalles."""
        insect_number = self.search_entry.get()
        if not insect_number.isdigit():
            messagebox.showerror("Error", "Ingrese un número de insecto válido.")
            return

        # Buscar el registro
        record = next((r for r in self.data if r["InsectNumber"] == insect_number), None)
        if record:
            self.display_record_details(record)
        else:
            messagebox.showinfo("No encontrado", "No se encontró el insecto con ese número.")

    def display_record_details(self, record):
        """Muestra los detalles del registro en la tabla de detalles."""
        # Limpiar la tabla de detalles antes de agregar el nuevo registro
        self.detail_table.clear_data()
        # Cargar el nuevo registro en la tabla de detalles
        self.detail_table.load_data([record])

    def refresh_data(self):
        """Recarga los datos desde la API y limpia la tabla principal."""
        new_data = self.api_client.get_data()
        self.table_widget.clear_data()  # Limpia los datos anteriores de la tabla principal
        self.load_data(new_data)  # Carga los nuevos datos en la tabla principal

    def run(self):
        """Inicia la aplicación."""
        self.window.mainloop()
