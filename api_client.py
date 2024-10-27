import requests

class APIClient:
    """Encapsula la lógica para conectarse y recuperar datos de la API."""

    BASE_URL = "https://671be4b62c842d92c381a9cc.mockapi.io/test"

    def get_data(self):
        """Obtiene los datos de la API y devuelve una lista de registros."""
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            return []
