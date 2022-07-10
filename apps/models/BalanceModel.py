from apps.models import Model


class Balance(Model):
    __table__ = 'balances'
    __primary_key__= 'id'
    __timestamps__ = False
    __fillable__ = ['id', 'amount', 'date']