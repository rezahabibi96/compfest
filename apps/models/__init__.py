from orator import DatabaseManager, Model, Schema
from apps.helper import Config, Log


database = Config.PARAMS.DATABASE
conf = {
    'postgresql': {
        'driver': 'postgres',
        'host': database.host,
        'database': database.db,
        'user': database.username,
        'password': database.password,
        'port': database.port,
        'prefix': ''
    }
}


db = DatabaseManager(conf)
schema = Schema(db)


Model.set_connection_resolver(db)