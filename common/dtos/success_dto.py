class SuccessDto:

    def __init__(self, msg):
        self.msg = msg

    def serialize(self):
        return {
            "msg": self.msg
        }
