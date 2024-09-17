from Libs.ConnTools import readConfig, generateConnUrl
import sqlalchemy as sa

config = readConfig("config-sqlite.yaml")  # Leer todas las configuraciones
config_source = config["source"]  # Leer solo la configuración de source

engine = sa.create_engine(generateConnUrl(config_source))

metadata = sa.MetaData()

user_table = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(50)),
    sa.Column("email", sa.String(50)),
)

# Crear tablas
metadata.create_all(engine)


def insert_user(name, email):
    query = user_table.insert().values(name=name, email=email)
    with engine.connect() as connection:
        with connection.begin():  # Explicitly start a transaction
            connection.execute(query)


def select_user(name):
    query = user_table.select().where(user_table.c.name == name)
    with engine.connect() as connection:
        result = connection.execute(query)
        return result.fetchone()


if __name__ == "__main__":
    # Insertar datos de prueba
    insert_user("Juan", "juan@gmail.com")
    insert_user("Pedro", "pedro@gmail.com")

    # Recuperar datos de prueba
    user = select_user("Juan")
    print(user)
