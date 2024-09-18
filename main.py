from Libs.ConnTools import readConfig, generateConnUrl
import sqlalchemy as sa

# Leer todas las configuraciones (considerando que podrias tener varias bases de datos)
config = readConfig("config-sqlite.yaml")

# Leer solo la configuración de conexion para source
config_source = config["source"]

# engine: objeto intermediario entre Python y la base de datos, puede:
# ejecutar consultas, crear conexiones, manejar transacciones, etc.
engine = sa.create_engine(generateConnUrl(config_source))

# metadata: contenedor para la definición de tablas y
# otros objetos relacionados con el esquema de la base de datos.
metadata = sa.MetaData()

user_table = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(50)),
    sa.Column("email", sa.String(50)),
)


def insert_user(name, email):
    query = user_table.insert().values(name=name, email=email)
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(query)


def select_user(name):
    query = user_table.select().where(user_table.c.name == name)
    with engine.connect() as connection:
        result = connection.execute(query)
        return result.fetchone()


if __name__ == "__main__":
    # Crear tablas de metadata
    metadata.create_all(engine)

    # Insertar datos de prueba
    insert_user("Juan", "juan@gmail.com")
    insert_user("Pedro", "pedro@gmail.com")

    # Recuperar datos de prueba
    user = select_user("Juan")
    print(user)
