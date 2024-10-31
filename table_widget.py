import tkinter as tk
from tkinter import ttk

class TableWidget:
    """Encapsula la tabla con estilo y barra de desplazamiento opcional."""

    def __init__(self, parent, slim=False, scroll=True):
        # Crear frame contenedor
        self.frame = tk.Frame(parent, bg="#f5f5f5", bd=2, relief="groove")

        # Estilo de la tabla
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview", background="#ffffff", rowheight=30, bordercolor="#999999", borderwidth=1)
        style.map("Custom.Treeview", background=[("selected", "#c1e4e9")])
        style.configure("Custom.Treeview.Heading", background="#4a7a8c", foreground="white", font=("Helvetica", 12, "bold"))

        # Crear la tabla
        self.tree = ttk.Treeview(
            self.frame,
            columns=("Insect", "RegistrationDate", "DiscoveryPlace", "InsectNumber"),
            show="headings",
            style="Custom.Treeview",
        )

        # Configurar encabezados y ancho de columnas
        column_width = 100 if slim else 150  # Ancho reducido para la tabla de detalles
        self.tree.heading("Insect", text="Insect")
        self.tree.heading("RegistrationDate", text="Registration Date")
        self.tree.heading("DiscoveryPlace", text="Discovery Place")
        self.tree.heading("InsectNumber", text="Insect Number")
        for col in ("Insect", "RegistrationDate", "DiscoveryPlace", "InsectNumber"):
            self.tree.column(col, width=column_width, anchor="center")

        # Barra de desplazamiento opcional
        if scroll:
            scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
            self.tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky="ns")

        # Ubicar widgets en el frame
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

    def load_data(self, data):
        """Carga los datos en la tabla con colores alternados."""
        for i, record in enumerate(data):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert(
                "", "end", values=(
                    record["Insect"],
                    record["RegistrationDate"],
                    record["DiscoveryPlace"],
                    record["InsectNumber"]
                ), tags=(tag,)
            )
        self.tree.tag_configure("evenrow", background="#f9f9f9")
        self.tree.tag_configure("oddrow", background="#e0f7fa")

    def clear_data(self):
        """Elimina todos los datos de la tabla."""
        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_frame(self):
        """Devuelve el frame del widget de la tabla."""
        return self.frame
