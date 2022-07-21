import os
import yaml
import binascii
from hashids import Hashids
from yaml.loader import Loader
from apps.helper import Log
from apps.schemas.SchemaConfig import ConfigApps


def decoder_app(code, salt):
    hashids = Hashids(salt=salt)
    text_hex = hashids.decode_hex(code)
    text = binascii.unhexlify(text_hex)
    text_str = str(text, 'utf-8')
    return text_str


def encoder_app(text, salt):
    hashids = Hashids(salt=salt)
    text = binascii.hexlify(text.encode())
    text_str = str(text, 'utf-8')
    text_hex = hashids.encode_hex(text_str)
    return text_hex


class Config:
    __dir_name__ = os.path.dirname(__file__)
    __file_path__ = '../../config/config.yaml'
    __file_config__ = os.path.abspath(os.path.join(__dir_name__, __file_path__))

    __config_yaml__ = None
    PARAMS = ConfigApps

    @classmethod
    def load(cls):
        config = open(cls.__file_config__, "r")
        cls.__config__yaml__ = None
        
        if yaml.load(config, Loader=Loader)['env'] == 'production':
            cls.__config__yaml__ = yaml.load(os.environ['CONFIG'])
            Log.debug('!!!!')
            Log.debug(cls.__config__yaml__)
        
        else:
            cls.__config__yaml__ = yaml.load(config, Loader=Loader)
        Log.debug('####')
        Log.debug(cls.__config_yaml__)
        
        Log.info("load config/config.yaml config !")

        cls.PARAMS = ConfigApps(
            ENVIRONMENT=cls.__config_yaml__['env'],
            INFORMATION=cls.__config_yaml__["apps"],
            ALLOWED_HOSTS=cls.__config_yaml__["allowed_hosts"],
            ALLOWED_METHODS=cls.__config_yaml__["allowed_methods"],
            STORAGE=cls.__config_yaml__["storage"][cls.__config_yaml__['env']],
            DATABASE=cls.__config_yaml__["database"][cls.__config_yaml__['env']],
            TOKEN=cls.__config_yaml__["token"][cls.__config_yaml__['env']],
            SALT=cls.__config_yaml__["salt"][cls.__config_yaml__['env']]
        )

        Log.info("config environment '{}' has loaded !".format(cls.__config_yaml__['env']))

    responses = {
        200: {
            "description": "Success get data",
            "content": {
                "application/json": {"example": {"status": 200, "message": "success", "data": []}}},
        },
        404: {
            "description": "Not Found",
            "content": {"application/json": {"example": {"status": 404, "message": "Not Found", "data": []}}},
        },
        403: {
            "description": "Not enough privileges",
            "content": {
                "application/json": {"example": {"status": 403, "message": "inappropriate privileges", "data": []}}},
        },
    }

    responses_home = {
        200: {
            "content": {
                "application/json": {
                    "example": {
                        "title": "API using fastAPI", "version": "1.0.0", "description": "API using fastAPI"
                    }
                }
            }
        } 
    }


Config.load()