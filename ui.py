import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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

        # Instancia del cliente API
        self.api_client = APIClient()

        # Tabla de registros
        self.table_widget = TableWidget(self.window)
        self.table_widget.get_frame().pack(expand=True, fill="both", pady=(10, 0))

        # Frame de búsqueda y refresco
        search_frame = tk.Frame(self.window, bg="#f5f5dc")
        search_frame.pack(pady=10)

        # Entrada de texto para el número de insecto
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=0, padx=5)

        # Botón de búsqueda
        search_button = tk.Button(
            search_frame, text="Buscar Insecto", command=self.search_record
        )
        search_button.grid(row=0, column=1, padx=5)

        # Botón de refresco de datos
        refresh_button = tk.Button(
            search_frame, text="Refrescar Datos", command=self.refresh_data
        )
        refresh_button.grid(row=0, column=2, padx=5)

        # Frame para mostrar detalles del insecto seleccionado en formato tabla
        self.detail_frame = tk.Frame(self.window, bg="#e0ffe0", bd=2, relief="groove")
        self.detail_frame.pack(fill="x", padx=10, pady=10)

        # Tabla para mostrar detalles del insecto seleccionado
        self.detail_table = ttk.Treeview(
            self.detail_frame,
            columns=("Insect", "RegistrationDate", "DiscoveryPlace", "InsectNumber"),
            show="headings",
            height=1
        )
        for col in ("Insect", "RegistrationDate", "DiscoveryPlace", "InsectNumber"):
            self.detail_table.heading(col, text=col)
            self.detail_table.column(col, anchor="center", width=150)

        # Posicionar la tabla en el frame de detalles
        self.detail_table.pack(fill="x", padx=10, pady=5)

        # Almacenar los datos cargados
        self.data = []

    def load_data(self, data):
        """Carga los datos en la tabla y los almacena."""
        self.data = data
        self.table_widget.load_data(data)

    def refresh_data(self):
        """Refresca los datos obteniéndolos de nuevo de la API."""
        try:
            new_data = self.api_client.get_data()
            self.load_data(new_data)
            messagebox.showinfo("Datos actualizados", "Los datos han sido actualizados correctamente.")
        except Exception as e:
            messagebox.showerror("Error de conexión", f"No se pudieron actualizar los datos: {e}")

    def search_record(self):
        """Busca un registro por el número de insecto."""
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
        """Muestra los detalles del registro en el frame de detalles en formato tabla."""
        # Limpiar la tabla de detalles antes de cargar nuevo registro
        for item in self.detail_table.get_children():
            self.detail_table.delete(item)

        # Insertar los detalles del insecto en la tabla
        self.detail_table.insert(
            "", "end", values=(
                record["Insect"],
                record["RegistrationDate"],
                record["DiscoveryPlace"],
                record["InsectNumber"]
            )
        )

    def run(self):
        """Inicia la aplicación."""
        self.window.mainloop()

