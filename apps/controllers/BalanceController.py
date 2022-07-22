from time import time
from datetime import datetime
from apps.helper import Log
from apps.models.BalanceModel import Balance
from apps.schemas import BaseResponse
from apps.schemas.SchemaBalance import RequestBalance, ResponseBalance



class ControllerBalance(object):
    @classmethod
    def withdraw_balance(cls, input_data=None):
        input_data = RequestBalance(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.amount is not None:
                data = Balance.first()

                if data:
                    if data.amount < input_data.amount:
                        result.message = "amount withdrawn must not bigger than current balance"
                    else:
                        amount = data.amount - input_data.amount
                        data.update({'amount':amount, 'date':datetime.now()})
                        data.save()
                        result.message = "success"
                else:
                    data = Balance()
                    result.message = "there currently empty balance"
                result.status = 200  
                result.data = ResponseBalance(**data.serialize())
                Log.info(result.message)
            else:
                e = "amount must not be empty!"
                Log.error(e)
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def add_balance(cls, input_data=None):
        input_data = RequestBalance(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.amount is not None:
                data = Balance.first()

                if data:
                    amount = data.amount + input_data.amount
                    data.update({'amount':amount, 'date':datetime.now()})
                    data.save()
                else:
                    data = Balance(amount=input_data.amount, date=datetime.now())
                    data.save()
                
                result.status = 200
                result.message = "success"
                result.data = ResponseBalance(**data.serialize())
                Log.info(result.message)
            else:
                e = "amount must not be empty!"
                Log.error(e)
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result