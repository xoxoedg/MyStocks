import json

from src import app


def handle_function_call(method_call):
    try:
        result = method_call()
    except ValueError:
        return app.response_class(response=json.dumps({"msg": "THIS IS A VALUE ERROR"}),
                                  status=401,
                                  mimetype='application/json')
    except NameError:
        return app.response_class(response=json.dumps({"msg": "THIS IS A NAME ERROR"}),
                                  status=403,
                                  mimetype='application/json')
    return app.response_class(response=json.dumps(result),
                              status=200,
                              mimetype='application/json')
