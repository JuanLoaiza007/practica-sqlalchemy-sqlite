# Practica SQLAlchemy con SQLite

Esta es una pequeña práctica de la librería SQLAlchemy con una base de datos SQLite, la idea es revisar el uso básico desde la conexión a la base de datos hasta la creación de modelos y ejecución de consultas.

## Instalación

Para el desarrollo de esta práctica se usó Python 3.8.20, se recomienda crear un entorno virtual para el desarrollo.

### Entorno virtual

Para crear un entorno virtual, ejecutar el siguiente comando:

```bash
python -m venv venv
```

Para activar el entorno virtual, ejecutar el siguiente comando:

```bash
source venv/bin/activate
```

### Dependencias

Las librerias usadas en esta práctica son:

- sqlalchemy
- pyyaml

Para instalar las dependencias necesarias, hacer pip install de cada una manualmente o ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la práctica, ejecutar el siguiente comando:

```bash
python main.py
```

## Práctica adicional usando PostgreSQL

Suponiendo que ya tienes el entorno virtual y las dependencias instaladas, puedes seguir los siguientes pasos:

0. **Instala la dependencia de psycopg2:** Usa el comando:

```bash
pip install psycopg2-binary
```

1.  **Crea una base de datos en PostgreSQL**. Ten presente el nombre, usuario y otros datos para la conexión.
2.  **Ajusta la información de conexión a la BD:** En el archivo `config-postgres.yaml`, cambia los valores necesarios para conectarte a tu base de datos.
3.  **Haz que se use la configuración de conexión:** En el archivo `main.py` cambia:

          config = readConfig("config-sqlite.yaml")

    Por:

          config = readConfig("config-postgres.yaml")

> [!CAUTION]
>
> Recuerda que en la vida real NO debes subir datos sensibles como información de conexión a una base de datos a un repositorio git, **en un proyecto real conserva tu archivo `config.yaml` seguro y privado en las exclusiones de .`gitignore`**.

4.  Ejecuta el archivo `main.py` y comprueba que se ha creado la tabla y los registros en la base de datos.
