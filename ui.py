import tkinter as tk
from tkinter import messagebox
from table_widget import TableWidget

class EntomologyApp:
    """Encapsula la ventana principal de la aplicación."""

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Entomology Record")
        self.window.geometry("640x600")
        self.window.resizable(False, False)
        self.window.configure(bg="#f5f5dc")

        # Tabla de registros
        self.table_widget = TableWidget(self.window)
        self.table_widget.get_frame().pack(expand=True, fill="both", pady=(10, 0))

        # Frame de búsqueda
        search_frame = tk.Frame(self.window, bg="#f5f5dc")
        search_frame.pack(pady=10)

        # Entrada de texto para el número de insecto
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=0, padx=5)

        # Botón de búsqueda
        search_button = tk.Button(
            search_frame, text="Buscar Insecto", command=self.search_record
        )
        search_button.grid(row=0, column=1)

        # Frame para mostrar detalles del insecto seleccionado
        self.detail_frame = tk.Frame(self.window, bg="#e0ffe0", bd=2, relief="groove")
        self.detail_frame.pack(fill="x", padx=10, pady=10)

        # Etiqueta inicial para mostrar que no hay selección
        self.detail_label = tk.Label(
            self.detail_frame, text="Selecciona un insecto para ver los detalles.",
            bg="#e0ffe0", anchor="w", font=("Arial", 12)
        )
        self.detail_label.pack(fill="x", padx=10, pady=5)

        # Almacenar los datos cargados
        self.data = []

    def load_data(self, data):
        """Carga los datos en la tabla y los almacena."""
        self.data = data
        self.table_widget.load_data(data)

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
        """Muestra los detalles del registro en el frame de detalles."""
        # Limpiar el contenido del frame de detalles
        for widget in self.detail_frame.winfo_children():
            widget.destroy()

        # Mostrar los detalles del insecto
        for key, value in record.items():
            detail = f"{key}: {value}"
            tk.Label(
                self.detail_frame, text=detail, bg="#e0ffe0", anchor="w", font=("Arial", 12)
            ).pack(fill="x", padx=10, pady=2)

    def run(self):
        """Inicia la aplicación."""
        self.window.mainloop()

