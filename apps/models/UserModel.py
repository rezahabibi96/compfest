from apps.models import Model


class User(Model):
    __table__ = 'users'
    __primary_key__= 'id'
    __timestamps__ = False
    __fillable__ = ['id', 'email', 'password']