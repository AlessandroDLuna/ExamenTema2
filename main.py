from api_client import APIClient
from ui import EntomologyApp

def main():
    # Crear instancia de la aplicación y del cliente API
    app = EntomologyApp()
    api_client = APIClient()

    # Obtener los datos y cargarlos en la tabla
    data = api_client.get_data()
    app.load_data(data)

    # Ejecutar la aplicación
    app.run()

if __name__ == "__main__":
    main()
