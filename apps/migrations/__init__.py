from os import environ
from yaml import safe_load


DATABASES = safe_load(environ['DB'])