import json

from flask import current_app
from src.common.exception_handling import StocksValueException


def respond(method_call):
    try:
        result = method_call()
    except NameError:
        return current_app.response_class(response=json.dumps({"msg": "THIS IS A NAME ERROR"}),
                                  status=403,
                                  mimetype='application/json')
    except StocksValueException as e:
        return current_app.response_class(response=json.dumps({"msg": "THIS IS A CUSTOM ERROR: " + e.msg}),
                                  status=403,
                                  mimetype='application/json')

    return current_app.response_class(response=(json.dumps(result)),
                              status=200,
                              mimetype='application/json')
