class Lab5Exception(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def get_error_messaage(self):
        return self.message