class StocksValueException(ValueError):

    def __init__(self, msg):
        self.msg = msg
        super(StocksValueException, self).__init__()
