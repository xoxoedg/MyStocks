import json

from src import app
from src.common.exception_handling import StocksValueException


def respond(method_call):
    try:
        result = method_call()
    except NameError:
        return app.response_class(response=json.dumps({"msg": "THIS IS A NAME ERROR"}),
                                  status=403,
                                  mimetype='application/json')
    except StocksValueException as e:
        return app.response_class(response=json.dumps({"msg": "THIS IS A CUSTOM ERROR: " + e.msg}),
                                  status=403,
                                  mimetype='application/json')

    return app.response_class(response=(json.dumps(result)),
                              status=200,
                              mimetype='application/json')
