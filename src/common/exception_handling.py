class StocksValueException(ValueError):

    def __init__(self, msg):
        self.msg = msg
        super(StocksValueException, self).__init__()


class StocksNotFoundError(NameError):

    def __init__(self, msg):
        self.msg = msg
        super(StocksNotFoundError, self).__init__()



