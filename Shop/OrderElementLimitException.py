class OrderElementLimitException(Exception):

    def __init__(self, allowed_limit, message=None, *args):
        self.allowed_limit = allowed_limit
        if message is None:
            message = f"Max allowed order limit is {self.allowed_limit}"
        super().__init__(message, *args)
