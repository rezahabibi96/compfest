from orator import DatabaseManager, Model
from apps.helper import Config, Log


database = Config.PARAMS.DATABASE
conf = {
    'postgresql': {
        'driver': 'postgres',
        'host': database.host,
        'database': database.db,
        'user': database.username,
        'password': database.password,
        'prefix': ''
    }
}

db = DatabaseManager(conf)
Model.set_connection_resolver(db)


Log.warn('db loaded')