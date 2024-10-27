import tkinter as tk
from tkinter import messagebox
from table_widget import TableWidget

class EntomologyApp:
    """Encapsula la ventana principal de la aplicación."""

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Entomology Record")
        self.window.geometry("640x480")
        self.window.resizable(False, False)
        self.window.configure(bg="#f5f5dc")

        # Tabla con los registros
        self.table_widget = TableWidget(self.window)
        self.table_widget.get_frame().pack(expand=True, fill="both", pady=(10, 0))

        # Frame para la barra de búsqueda
        search_frame = tk.Frame(self.window, bg="#f5f5dc")
        search_frame.pack(pady=10)

        # Entrada de texto para buscar por número de insecto
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=0, padx=5)

        # Botón de búsqueda
        search_button = tk.Button(
            search_frame, text="Buscar Insecto", command=self.search_record
        )
        search_button.grid(row=0, column=1)

        # Almacenar los datos cargados
        self.data = []

    def load_data(self, data):
        """Carga los datos en la tabla y los almacena."""
        self.data = data
        self.table_widget.load_data(data)

    def search_record(self):
        """Busca y muestra un registro basado en el número de insecto."""
        insect_number = self.search_entry.get()
        if not insect_number.isdigit():
            messagebox.showerror("Error", "Ingrese un número de insecto válido.")
            return

        # Buscar el registro
        record = next((r for r in self.data if r["InsectNumber"] == insect_number), None)
        if record:
            self.show_record_popup(record)
        else:
            messagebox.showinfo("No encontrado", "No se encontró el insecto con ese número.")

    def show_record_popup(self, record):
        """Muestra una ventana emergente con los detalles del registro."""
        popup = tk.Toplevel(self.window)
        popup.title(f"Insecto: {record['Insect']}")
        popup.geometry("300x200")
        popup.configure(bg="#e0ffe0")

        # Mostrar los detalles del insecto
        for i, (key, value) in enumerate(record.items()):
            tk.Label(popup, text=f"{key}: {value}", bg="#e0ffe0", anchor="w").pack(
                fill="x", padx=10, pady=5
            )

    def run(self):
        """Inicia la aplicación."""
        self.window.mainloop()
