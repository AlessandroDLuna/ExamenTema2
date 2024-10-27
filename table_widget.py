import tkinter as tk
from tkinter import ttk

class TableWidget:
    """Encapsula la tabla con estilo y barra de desplazamiento."""

    def __init__(self, parent):
        # Crear frame contenedor
        self.frame = tk.Frame(parent, bg="#f5f5f5", bd=2, relief="groove")

        # Estilo de la tabla
        style = ttk.Style()
        style.theme_use("clam")  # Tema visual claro y moderno
        style.configure(
            "Custom.Treeview",
            background="#ffffff",  # Fondo blanco para filas normales
            fieldbackground="#f0f0f0",  # Fondo del área de entrada
            foreground="#000000",  # Texto negro
            rowheight=30,  # Altura de las filas
            bordercolor="#999999",  # Bordes grises
            borderwidth=1,
        )
        style.map("Custom.Treeview", background=[("selected", "#c1e4e9")])  # Selección azulada

        # Estilo para encabezados
        style.configure(
            "Custom.Treeview.Heading",
            background="#4a7a8c",  # Fondo azul
            foreground="white",  # Texto blanco
            font=("Helvetica", 12, "bold"),
        )

        # Crear la tabla (Treeview)
        self.tree = ttk.Treeview(
            self.frame,
            columns=("Insect", "RegistrationDate", "DiscoveryPlace", "InsectNumber"),
            show="headings",
            style="Custom.Treeview",
        )

        # Configurar encabezados
        self.tree.heading("Insect", text="Insect")
        self.tree.heading("RegistrationDate", text="Registration Date")
        self.tree.heading("DiscoveryPlace", text="Discovery Place")
        self.tree.heading("InsectNumber", text="Insect Number")

        # Ajustar ancho de columnas
        for col in ("Insect", "RegistrationDate", "DiscoveryPlace", "InsectNumber"):
            self.tree.column(col, width=150, anchor="center")

        # Crear barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        # Ubicar widgets en el frame
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Configuración del layout del frame
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

    def load_data(self, data):
        """Carga los datos en la tabla con colores alternados."""
        for i, record in enumerate(data):
            # Aplicar color alternado a las filas
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert(
                "", "end", values=(
                    record["Insect"],
                    record["RegistrationDate"],
                    record["DiscoveryPlace"],
                    record["InsectNumber"]
                ), tags=(tag,)
            )

        # Configurar los estilos de las filas
        self.tree.tag_configure("evenrow", background="#f9f9f9")
        self.tree.tag_configure("oddrow", background="#e0f7fa")

    def get_frame(self):
        """Devuelve el frame del widget de la tabla."""
        return self.frame
