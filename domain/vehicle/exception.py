class BrandCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message

class ModelCannotBeEmpty(Exception):
    def __init__(self, message):
        self.message = message
