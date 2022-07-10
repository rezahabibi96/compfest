from apps.models import Model


class Product(Model):
    __table__ = 'products'
    __primary_key__= 'id'
    __timestamps__ = False
    __fillable__ = ['id', 'name', 'price', 'desc', 'imagepath', 'timestamp']