import json

from src import app


def handle_function_call(method_call):
    try:
        result = method_call()
    except NameError:
        return app.response_class(response=json.dumps({"msg": "THIS IS A NAME ERROR"}),
                                  status=403,
                                  mimetype='application/json')
    except StocksValueException as e:
        return app.response_class(response=json.dumps({"msg": "THIS IS A NAME ERROR " + e.msg}),
                                  status=403,
                                  mimetype='application/json')
    return app.response_class(response=json.dumps(result),
                              status=200,
                              mimetype='application/json')


class StocksValueException(ValueError):

    def __init__(self, msg):
        self.msg = msg
        super(StocksValueException, self).__init__()