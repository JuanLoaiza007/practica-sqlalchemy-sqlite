import yaml


def readConfig(configFile: str) -> dict:
    """
    Función para leer el archivo de configuración

    Args:
        configFile (str): Ruta al archivo de configuración

    Returns:
        dict: Configuración del archivo de configuración
    """
    with open(configFile, "r") as file:
        return yaml.safe_load(file)


def generateConnUrl(config: dict) -> str:
    """
    Función para generar la url de conexión a la base de datos
    usando la configuración

    Args:
        config (dict): Configuración del archivo de configuración

    Returns:
        str: Url de conexión a la base de datos
    """

    driver = config["driver"]

    if driver != "sqlite":
        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]

    database = config["database"]

    if driver == "sqlite":
        return f"{driver}:///{database}"
    elif driver == "postgresql":
        return f"{driver}://{username}:{password}@{host}:{port}/{database}"
    else:
        raise Exception("Driver not supported")
